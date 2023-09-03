from django.urls import path, include
from .views import *
urlpatterns = [
    path('', PostList.as_view()),
    # path('<int:pk>/', TripDetail.as_view()),
]
