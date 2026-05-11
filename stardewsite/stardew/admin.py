from django.contrib import admin
from .models import Season, FarmingItem, ForagingItem, FishingItem, Bundle, BundleItem
import csv
from django.http import HttpResponse
# Register your models here.
# Models registered

# Function for exporting the farming items to a csv file -- added in module 8
def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=farmingitemexport.csv"
    writer = csv.writer(response)
    writer.writerow(["name", "sell_price", "season", "growth_time"])
    for obj in queryset:
        writer.writerow([obj.name, obj.sell_price, obj.season, obj.growth_time])
    return response

export_as_csv.short_description = "Export selected to CSV"


admin.site.register(Season)

# Added in module 8 for exporting csv
@admin.register(FarmingItem)
class FarmingItemAdmin(admin.ModelAdmin):
    #  3.06 custom admin action !!!
    actions = [export_as_csv]

admin.site.register(ForagingItem)
admin.site.register(FishingItem)

@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    list_display = ['name', 'room']

@admin.register(BundleItem)
class BundleItemAdmin(admin.ModelAdmin):
    list_display = ['bundle', 'item', 'quantity_required', 'donated']


