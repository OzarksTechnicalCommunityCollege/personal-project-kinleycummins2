from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FarmingItem, FishingItem
 
#  Signal for when farming item is added
@receiver(post_save, sender=FarmingItem)
def log_farming_item_saved(sender, instance, created, **kwargs):
    if created:
        print(f'[Signal] New farming item added: {instance.name}')
 
#  Signal for when fishing item is added
@receiver(post_save, sender=FishingItem)
def log_fishing_item_saved(sender, instance, created, **kwargs):
    if created:
        print(f'[Signal] New fishing item added: {instance.name}')
 