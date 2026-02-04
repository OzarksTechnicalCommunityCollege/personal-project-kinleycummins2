from django.db import models
# Not currently in use, may implement later?
from taggit.managers import TaggableManager

# Create your models here.
# Revamped models compared to Module 2 - Now sorting things by season
# This will be much better for UI purposes and 
class Season(models.Model):
    name = models.CharField(
        max_length=10,
        unique=True,
        choices=[
            ("spring", "Spring"),
            ("summer", "Summer"),
            ("fall", "Fall"),
            ("winter", "Winter"),
        ]
    )
    def __str__(self):
        return self.name.title

# This class is created to be a 'template' for the other models, hence why it is abstract
class SeasonalItem(models.Model):
    name = models.CharField(max_length=100)
    sell_price = models.PositiveIntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
# Taking inspiration from an old/outdated helper site and sorting things by forge, farming, and fishing for each season
class FarmingItem(SeasonalItem):
    growth_time = models.PositiveIntegerField()
# Not actively being used yet just for testing simplicity
class ForagingItem(SeasonalItem):
    pass

# Not actively being used yet just for testing simplicity   
class FishingItem(SeasonalItem):
    pass