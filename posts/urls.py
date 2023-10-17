from django.urls import path, include
from .views import PostDetail,AcquisCreateList, LostCreateList
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register(r'', PostList, basename='list')


urlpatterns = [
    path('lost/', LostCreateList.as_view()),
    path('acquis/', AcquisCreateList.as_view()),
    path('', AcquisCreateList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
