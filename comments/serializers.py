from rest_framework import serializers
from .models import *
from django.utils import timezone


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
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
            return f"{days} days, {hours} hours, {minutes} minutes ago"
        elif hours > 0:
            return f"{hours} hours, {minutes} minutes ago"
        elif minutes > 0:
            return f"{minutes} minutes ago"
        else:
            return "Just now"