from rest_framework import generics
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        place = request.query_params.getlist('place')
        color = request.query_params.getlist('color')
        type = request.query_params.getlist('type')

        queryset = self.get_queryset()

        # Q 객체를 사용하여 모든 조건을 만족하는 포스트 필터링
        conditions = Q()
        
        for p in place:
            conditions |= Q(place__icontains=p)
        
        for c in color:
            conditions |= Q(color__icontains=c)

        for t in type:
            conditions |= Q(type__icontains=t)

        queryset = queryset.filter(conditions)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer