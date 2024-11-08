from rest_framework import viewsets
from .models import *
from .serializers import *


class PredictionImageViewSet(viewsets.ModelViewSet):
    queryset = PredictionImage.objects.all()
    serializer_class = PredictionImageSerializer


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
