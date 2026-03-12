from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Season, FarmingItem, ForagingItem, FishingItem
from .forms import LoginForm, UserRegistrationForm
# Create your views here.
# ***********MODULE 6 - NEED TO ADD IN PREFETCHING**********
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

# Home page view
def home(request):
    return render(request, "stardew/home.html")

# Dashboard -- Keeping for now
@login_required
def dashboard(request):
    return render(
        request,
        'stardew/registration/dashboard.html'
    )

# Register view
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object
            new_user = user_form.save(commit=False)

            # set password
            new_user.set_password(
                user_form.cleaned_data['password']
            )

            # save user
            new_user.save()

            user = authenticate(
                username=new_user.username,
                password=user_form.cleaned_data['password']
            )

            login(request, user)
            return redirect('home')
    
    else:
        user_form = UserRegistrationForm()
        return render(
            request,
            'registration/registration.html',
            {'user_form': user_form}
        )
# Login view
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 request,
#                 username = cd['username'],
#                 password = cd['password']
#             )
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#         else:
#             form = LoginForm()
#             return render(request, 'stardew/login/login.html', {'form':form})


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