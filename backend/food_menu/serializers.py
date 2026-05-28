from rest_framework import serializers
from .models import FoodMenu


class FoodMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodMenu
        fields = '__all__'