from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("images", PredictionImageViewSet)
router.register("predictions-upload", PredictionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("upload/", prediction_upload, name="prediction-upload"),
]
