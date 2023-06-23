from rest_framework import serializers
from .models import Food, Consume


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class ConsumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consume
        fields = "__all__"