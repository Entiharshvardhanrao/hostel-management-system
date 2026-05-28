from django.urls import path
from .views import FoodMenuListCreateView

urlpatterns = [
    path('food-menu/', FoodMenuListCreateView.as_view()),
]