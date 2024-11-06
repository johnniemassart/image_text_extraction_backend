from rest_framework import serializers
from .models import *


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ["id", "image_url"]

    # def create(self, validated_data):
    #     pass
