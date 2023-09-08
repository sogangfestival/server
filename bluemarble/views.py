from rest_framework.viewsets import ModelViewSet
from .serializers import BuildingSerializer
from .models import Building

class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer