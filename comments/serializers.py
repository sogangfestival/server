from rest_framework import serializers
from .models import *
from django.utils import timezone


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    writer = serializers.CharField(max_length=100, required=False)  # writer 필드를 선택 사항으로 변경

    class Meta:
        model = Comment
        fields = '__all__'

    def get_created_at(self, obj):
        now = timezone.now()
        time_difference = now - obj.created_at
        days = time_difference.days
        seconds = time_difference.seconds

        hours, remainder = divmod(seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        if days > 0:
            return f"{days} days {hours} hours {minutes} minutes ago"
        elif hours > 0:
            return f"{hours} hours {minutes} minutes ago"
        elif minutes > 0:
            return f"{minutes} minutes ago"
        else:
            return "Just now"
    
    def create(self, validated_data):
        post = validated_data['post']
        request = self.context['request']
        password = int(request.data.get('password'))
        post_password = post.password

        writer = None
        if post_password == password:
            writer = '작성자'
        else:
            comments_count = Comment.objects.filter(post=post).exclude(writer='작성자').count() + 1
            writer = f'알로스{comments_count}'
        
        # "writer" 필드를 설정하고 validated_data에서 제거
        validated_data['writer'] = writer
        return super().create(validated_data)