from rest_framework import serializers, fields
from .models import *
from .models import PLACES_CHOICES, TYPE_CHOICES, COLOR_CHOICES
from comments.models import Comment
from django.utils import timezone
from datetime import datetime



class PostSerializer(serializers.ModelSerializer):
    place = serializers.MultipleChoiceField(choices=PLACES_CHOICES)
    type = serializers.MultipleChoiceField(choices=TYPE_CHOICES)
    color = serializers.MultipleChoiceField(choices=COLOR_CHOICES)
    created_at = serializers.SerializerMethodField() 
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
    
    def get_comment_count(self, obj):
        return obj.comment_post.count()
    
    def get_created_at(self, obj):
        now = datetime.now()
        obj_created_at = datetime.combine(obj.created_at, datetime.min.time())

        time_difference = now - obj_created_at
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

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    sub_comments = serializers.SerializerMethodField(read_only=True)

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

    def get_sub_comments(self, obj):
        sub_comments = Comment.objects.filter(parent_comment=obj)
        return CommentSerializer(sub_comments, many=True).data

class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    place = serializers.MultipleChoiceField(choices=PLACES_CHOICES)
    type = serializers.MultipleChoiceField(choices=TYPE_CHOICES)
    color = serializers.MultipleChoiceField(choices=COLOR_CHOICES)
    created_at = serializers.SerializerMethodField() 

    class Meta:
        model = Post
        fields = '__all__'
    def get_created_at(self, obj):
        now = datetime.now()
        obj_created_at = datetime.combine(obj.created_at, datetime.min.time())

        time_difference = now - obj_created_at
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