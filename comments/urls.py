from django.urls import path, include
from .views import *
urlpatterns = [
    path('', CommentListCreate.as_view()),
    path('<int:pk>/', CommentDetail.as_view()),
]
