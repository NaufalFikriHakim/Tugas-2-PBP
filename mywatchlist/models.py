from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField(default=False)
    title = models.TextField()
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    release_date = models.TextField()
    review = models.TextField()