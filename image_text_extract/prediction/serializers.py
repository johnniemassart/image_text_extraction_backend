from rest_framework import serializers
from .models import *
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# from PIL import Image


class PredictionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionImage
        fields = ["id", "prediction", "image_url"]


class PredictionSerializer(serializers.ModelSerializer):
    images = PredictionImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=10000),
        required=False,
        allow_empty=True,
        write_only=True,
    )

    class Meta:
        model = Prediction
        fields = ["id", "title", "images", "uploaded_images"]

    def create(self, validated_data):
        if validated_data.get("uploaded_images") is not None:
            uploaded_images = validated_data.pop("uploaded_images")
            prediction = Prediction.objects.create(**validated_data)
            for img in uploaded_images:
                uploaded_result = cloudinary.uploader.upload(
                    img, folder="image_to_text"
                )
                PredictionImage.objects.create(
                    prediction=prediction, image_url=uploaded_result["secure_url"]
                )
        else:
            prediction = Prediction.objects.create(**validated_data)
        return prediction
