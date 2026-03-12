from django.db import models
# from taggit.managers import TaggableManager

# Create your models here.
# Revamped models compared to Module 2 - Now sorting things by season
# This will be much better for UI purposes and sorting later
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
        return self.name.title()

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

# Will add more to this later
class ForagingItem(SeasonalItem):
    pass

# Will add more to this later  
class FishingItem(SeasonalItem):
    pass

# Represents a community center bundle
class Bundle(models.Model):

    ROOM_CHOICES = [
        ("crafts_room", "Crafts Room"),
        ("pantry", "Pantry"),
        ("fish_tank", "Fish Tank"),
        ("boiler_room", "Boiler Room"),
        ("bulletin_board", "Bulletin Board"),
        ("vault", "Vault"),
    ]
 
    name = models.CharField(max_length=100)
    room = models.CharField(max_length=50, choices=ROOM_CHOICES)
 
    def __str__(self):
        return self.name
 
# Intermediary table that links a CC bundle to a farming item, foraging item, or fishing item
# Also uses nullable FKs so any item type can be linked
class BundleItem(models.Model):

    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE, related_name="bundle_items")
 
    # Only one of these will be set per row
    farming_item = models.ForeignKey(FarmingItem, null=True, blank=True, on_delete=models.CASCADE)
    foraging_item = models.ForeignKey(ForagingItem, null=True, blank=True, on_delete=models.CASCADE)
    fishing_item = models.ForeignKey(FishingItem, null=True, blank=True, on_delete=models.CASCADE)
 
    # Custom fields on the intermediary table
    quantity_required = models.PositiveIntegerField(default=1)
    donated = models.BooleanField(default=False)
 
    def __str__(self):
        item = self.farming_item or self.foraging_item or self.fishing_item
        return f"{item} x{self.quantity_required} -> {self.bundle}"
# Property to get whatever item is linked
    @property
    def item(self):
        return self.farming_item or self.foraging_item or self.fishing_item