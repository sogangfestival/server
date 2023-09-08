from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', PostList, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', PostDetail.as_view()),
]