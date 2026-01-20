from django.db import models

# Create your models here.
# Model for the crops in game
class Crop(models.Model):
    name = models.CharField(max_length=40)
    season = models.CharField(max_length=20)
    growth_time = models.IntegerField()
    sell_price = models.IntegerField()

    def __str__(self):
        return self.name