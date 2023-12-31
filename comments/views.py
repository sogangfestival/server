from rest_framework import generics,status
from .models import *
from .serializers import *
from datetime import datetime
from rest_framework.response import Response

# Create your views here.
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create_comment(self, serializer):
        post_id = self.request.data.get('post_id')
        password = int(self.request.data.get('password'))
        content = self.request.data.get('content')
        post = Post.objects.get(pk=post_id)

        #대댓글이라면 대댓글의 parent_comment_id에 댓글 id 저장
        parent_comment_id = self.request.data.get('parent_comment')
        
        if parent_comment_id is not None:
            parent_comment = Comment.objects.get(pk=parent_comment_id)
        else:
            parent_comment = None
        serializer.save(post=post, password=password, parent_comment=parent_comment, content=content, created_at=datetime.now())
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        comment_id = kwargs["pk"]
        comment = Comment.objects.get(id=comment_id)
        serializer = self.get_serializer(comment)
        replys = []
        cocomments = Comment.objects.filter(parent_comment=comment_id)
        for cocomment in cocomments:
            reply = self.get_serializer(cocomment)
            replys.append(reply.data)
        data = serializer.data 
        data["subcomments"] = replys
        return Response(data)