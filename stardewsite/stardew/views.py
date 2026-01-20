from django.shortcuts import render
from .models import Crop
# Create your views here.

# View for the crop list - added a filter to sort by season (will use later when I add more crops)
def crop_list(request):
    crops = Crop.objects.filter(season = "Spring")
    return render(request, "stardew/crop/list.html", {"crops": crops})