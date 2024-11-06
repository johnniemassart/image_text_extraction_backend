from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PredictionViewSet

router = DefaultRouter()
router.register("", PredictionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
