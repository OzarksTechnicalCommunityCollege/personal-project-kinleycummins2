from django.contrib import admin
from .models import Season, FarmingItem, ForagingItem, FishingItem
# Register your models here.
# Models registered
admin.site.register(Season)
admin.site.register(FarmingItem)
admin.site.register(ForagingItem)
admin.site.register(FishingItem)
