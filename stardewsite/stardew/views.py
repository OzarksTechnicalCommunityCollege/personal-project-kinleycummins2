from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Crop
from .forms import CropForm
# Create your views here.

# View for the crop list
def crop_list(request):
    # Getting all of the crops and sorting them by season, then by name
    crops = Crop.objects.all().order_by('season','name')

    # For organization purposes, the crops are sorted into a dictionary
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    crops_by_season = {season: [] for season in seasons}
    for crop in crops:
        crops_by_season[crop.season].append(crop)
    return render(request, "stardew/crop/list.html", {"crops_by_season": crops_by_season})

# Function for adding the crop from the form
def add_crop(request):
    if request.method == "POST":
        form = CropForm(request.POST)
        # Validating the form
        if form.is_valid():
            form.save()
            url = reverse("stardew:crop-list")
            # Technically don't need to use reverse here, could just redirect but wanted to try and implement it
            # May end up being changed later
            return redirect(url) 
        
    else:
        # Showing an empty form
        form = CropForm()

    return render(request, "stardew/crop/add.html", {"form": form})