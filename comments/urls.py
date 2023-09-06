from django.urls import path, include
from .views import *
urlpatterns = [
    path('', CommentList.as_view()),
    path('<int:pk>/', CommentDetail.as_view()),
    # path('<int:pk>/', TripDetail.as_view()),
]