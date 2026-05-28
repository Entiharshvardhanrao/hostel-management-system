from rest_framework import generics
from .models import FoodMenu
from .serializers import FoodMenuSerializer


class FoodMenuListCreateView(generics.ListCreateAPIView):
    queryset = FoodMenu.objects.all()
    serializer_class = FoodMenuSerializer