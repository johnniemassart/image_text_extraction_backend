from django.db import models


class Prediction(models.Model):
    image_url = models.URLField()

    def __str__(self):
        return self.image_url
