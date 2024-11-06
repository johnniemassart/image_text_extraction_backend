from rest_framework import viewsets
from .models import *
from .serializers import *


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
