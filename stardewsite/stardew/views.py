from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Season, FarmingItem, ForagingItem, FishingItem
# from .forms import CropForm ****** commented out due to it not being fixed yet
# Create your views here.

# View for the sesason list
def season_list(request):
    seasons = Season.objects.all()

    season_data = []

    for season in seasons:
        season_data.append({
            "season": season,
            "farming": FarmingItem.objects.filter(season=season),
            "foraging": ForagingItem.objects.filter(season=season),
            "fishing": FishingItem.objects.filter(season=season),
        })

    return render(request, "stardew/season/list.html", {"season_data": season_data})

# # Function for adding the crop from the form
# def add_crop(request):
#     if request.method == "POST":
#         form = CropForm(request.POST)
#         # Validating the form
#         if form.is_valid():
#             form.save()
#             url = reverse("stardew:crop-list")
#             # Technically don't need to use reverse here, could just redirect but wanted to try and implement it
#             # May end up being changed later
#             return redirect(url) 
        
#     else:
#         # Showing an empty form
#         form = CropForm()

#     return render(request, "stardew/crop/add.html", {"form": form})