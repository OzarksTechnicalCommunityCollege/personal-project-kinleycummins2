from django.contrib import admin
from .models import Season, FarmingItem, ForagingItem, FishingItem, Bundle, BundleItem
# Register your models here.
# Models registered
admin.site.register(Season)
admin.site.register(FarmingItem)
admin.site.register(ForagingItem)
admin.site.register(FishingItem)

@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    list_display = ['name', 'room']

@admin.register(BundleItem)
class BundleItemAdmin(admin.ModelAdmin):
    list_display = ['bundle', 'item', 'quantity_required', 'donated']
