from rest_framework import serializers, fields
from .models import *
from .models import PLACES_CHOICES, TYPE_CHOICES, COLOR_CHOICES

class PostSerializer(serializers.ModelSerializer):
    place = serializers.MultipleChoiceField(choices=PLACES_CHOICES)
    type = serializers.MultipleChoiceField(choices=TYPE_CHOICES)
    color = serializers.MultipleChoiceField(choices=COLOR_CHOICES)
    class Meta:
        model = Post
        fields = '__all__'