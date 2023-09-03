from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer