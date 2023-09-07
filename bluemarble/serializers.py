from rest_framework.serializers import ModelSerializer
from .models import Building

class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'