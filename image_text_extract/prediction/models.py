from django.db import models


class Prediction(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PredictionImage(models.Model):
    prediction = models.ForeignKey(
        Prediction, on_delete=models.CASCADE, related_name="images", null=True
    )
    image_url = models.URLField()

    def __str__(self):
        return self.image_url
