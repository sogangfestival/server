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
            #flag 1 용
            
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
            # print(self.get_serializer(queryset, many=True).data)
            flag0_objects = queryset.filter(flag=False)
            flag1_objects = queryset.filter(flag=True)
            flag0_objects = flag0_objects.order_by('created_at')
            flag1_objects = flag1_objects.order_by('created_at')



            # 결과를 딕셔너리에 추가
            
        except Exception as e:
            return Response({'message': 'Filtering Error Occured, Sorry'}, status=status.HTTP_404_NOT_FOUND)

        result = {}
        try :
            flag0_page = self.paginate_queryset(flag0_objects)
            flag0_serializer = self.get_serializer(flag0_page, many=True)
            result["lost"] = flag0_serializer.data
        except Exception as e:
            result["lost"] = []
        try :
            flag1_page = self.paginate_queryset(flag1_objects)
            flag1_serializer = self.get_serializer(flag1_page, many=True)
            result["acquisition"] = flag1_serializer.data
        except Exception as e:
            result["acquisition"] = []
        return self.get_paginated_response(result)        





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
            


