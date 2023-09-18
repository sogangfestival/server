import json
from rest_framework import generics
from .models import *
from .serializers import *
from django.db.models import Q
from rest_framework.response import Response
from comments.models import Comment
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import DocumentForm

class Paginated(PageNumberPagination):
    page_size =4
    page_size_query_param = 'page_size'
    max_page_size =4

@method_decorator(csrf_exempt, name="dispatch")
class LostCreateList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = Paginated
    # filter 기능
    def create(self, request, *args, **kwargs):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponse(json.dumps({"status": "Success"}))
        else:
            return HttpResponse(json.dumps({"status": "Failed"}))
        
    def list(self, request, *args, **kwargs):
        place = request.query_params.getlist('place', [])
        color = request.query_params.getlist('color', [])
        type = request.query_params.getlist('type', [])
        keyword = request.query_params.get('keyword', None)

        queryset = self.get_queryset()
        queryset = queryset.filter(flag=True)
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
            queryset = queryset.order_by('-created_at')

        except Exception as e:
            return Response({'message': 'Filtering Error Occured, Sorry'}, status=status.HTTP_404_NOT_FOUND)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@method_decorator(csrf_exempt, name="dispatch")
class AcquisCreateList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = Paginated
    
    def create(self, request, *args, **kwargs):
        form = DocumentForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponse(json.dumps({"status": "Success"}))
        else:
            return HttpResponse(json.dumps({"status": "Failed"}))

    # filter 기능
    def list(self, request, *args, **kwargs):
        place = request.query_params.getlist('place', [])
        color = request.query_params.getlist('color', [])
        type = request.query_params.getlist('type', [])
        keyword = request.query_params.get('keyword', None)

        queryset = self.get_queryset()
        queryset = queryset.filter(flag=False)
        try:
            # Q 객체를 사용하여 모든 조건을 만족하는 포스트 필터
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
            queryset = queryset.order_by('-created_at')
            print(queryset)

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


@method_decorator(csrf_exempt, name="dispatch")
def model_form_upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({"status": "Success"}))
        else:
            return HttpResponse(json.dumps({"status": "Failed"}))