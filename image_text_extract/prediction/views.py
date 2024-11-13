from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import ml_image_text_algo.ml_image_text_extract as ml


class PredictionImageViewSet(viewsets.ModelViewSet):
    queryset = PredictionImage.objects.all()
    serializer_class = PredictionImageSerializer


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer


# function based views
@api_view(["GET", "POST"])
def prediction_upload(request):
    if request.method == "GET":
        predictions = Prediction.objects.all()
        serializer = PredictionSerializer(predictions, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            prediction = serializer.save()
            uploaded_images = prediction.images.all()
            img_responses = []
            for img in uploaded_images:
                img_responses.append(ml.img_response(img))
            return Response(
                {"message": img_responses, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
