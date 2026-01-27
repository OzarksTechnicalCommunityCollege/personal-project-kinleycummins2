from django.db import models

# Create your models here.
# Model for the crops in game
# Created a base crop class that will be inheritated 
class BaseCrop(models.Model):
    name = models.CharField(max_length=60)
    season = models.CharField(max_length=20)
    growth_time = models.IntegerField()

    class Meta:
        # Setting abstract to true will mean that no database table is created for both the parent class and child class
        abstract = True
    def __str__(self):
        return self.name

class Crop(BaseCrop):
    sell_price = models.IntegerField()