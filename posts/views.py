from rest_framework import generics
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # filter 기능
    def get(self, request, *args, **kwargs):
        place = request.query_params.get('place', '')  # 기본값으로 빈 문자열을 설정
        color = request.query_params.get('color', '')  # 기본값으로 빈 문자열을 설정
        type = request.query_params.get('type', '') # 기본값으로 빈 문자열을 설정
        print(place, color, type)
        queryset = self.get_queryset() 
        try:
            if place:
                queryset = queryset.filter(place=place)
                print(queryset)
            if color:
                queryset = queryset.filter(color=color)
                print(queryset)
            if type:
                queryset = queryset.filter(type=type)
                print(queryset)

        except Exception as e:
            return Response({'message': 'Filtering Error Occured, Sorry'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
