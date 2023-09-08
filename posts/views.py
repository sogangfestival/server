from rest_framework import generics
from .models import *
from .serializers import *
from django.db.models import Q
from rest_framework.response import Response
from comments.models import Comment
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

class Paginated(PageNumberPagination):
    page_size =4
    page_size_query_param = 'page_size'
    max_page_size =4

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = Paginated

    # filter 기능
    def list(self, request, *args, **kwargs):
        place = request.query_params.getlist('place', [])
        color = request.query_params.getlist('color', [])
        type = request.query_params.getlist('type', [])
        keyword = request.query_params.get('keyword', None)

        queryset = self.get_queryset()
        try:
            # Q 객체를 사용하여 모든 조건을 만족하는 포스트 필터링
            conditions = Q()
            
            for p in place:
                conditions &= Q(place__icontains=p)
            
            for c in color:
                conditions &= Q(color__icontains=c)

            for t in type:
                conditions &= Q(type__icontains=t)
            if keyword:
                conditions &= Q(title__icontains=keyword)
                print(keyword)

            queryset = queryset.filter(conditions)
        except Exception as e:
            return Response({'message': 'Filtering Error Occured, Sorry'}, status=status.HTTP_404_NOT_FOUND)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   




class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def get(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_detail = Post.objects.get(id=post_id)
        # parent_comment가 null인 주요 댓글 조회
        main_comments = Comment.objects.filter(post=post_detail, parent_comment=None)
        main_comments_data = CommentSerializer(main_comments, many=True).data
        data = self.get_serializer(post_detail).data
        data['comments'] = main_comments_data
        return Response(data)
            


