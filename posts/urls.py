from django.urls import path, include
from .views import PostDetail,PostList
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register(r'', PostList, basename='list')


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
]