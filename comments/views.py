from rest_framework import generics
from .models import *
from .serializers import *
from datetime import datetime
from rest_framework.response import Response

# Create your views here.
class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create_comment(self, serializer):
        post_id = self.request.data.get('post_id')
        password = self.request.data.get('password')
        content = self.request.data.get('content')

        post = Post.objects.get(pk=post_id)
        
        #작성자 이름 만들어주기
        if post.password == password:
            # serializer.validated_data['writer'] = '작성자'
            writer = '작성자'
        else:
            comments_count = Comment.objects.filter(post=post).exclude(writer='작성자').count() + 1
            # serializer.validated_data['writer'] = f'알로스{comments_count}'
            writer = f'알로스{comments_count}'

        #대댓글이라면 대댓글의 parent_comment_id에 댓글 id 저장
        parent_comment_id = self.request.data.get('parent_comment')

        serializer.save(post=post, writer=writer,parent_comment=parent_comment_id, content=content, created_at=datetime.now())

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