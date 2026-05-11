from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Season, FarmingItem, ForagingItem, FishingItem, Bundle, BundleItem
from .forms import LoginForm, UserRegistrationForm
from .bundle_tracker import BundleTracker
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
    
# main community center tracker list
# loads all bundles with their items and passes the session tracker to template to render
def community_center(request):
    tracker = BundleTracker(request.session)

    # prefetch_related avoids N+1 queries!!!
    # loads all bundle items in one query instead of one per bundle in the template loop
    bundles = Bundle.objects.prefetch_related('bundle_items').all()

    # Convert to list so we can pass it to percent_complete
    bundle_list = list(bundles)

    completed_bundle_ids = {
        b.id for b in bundle_list 
        if b.bundle_items.exists() and tracker.is_bundle_complete(b)
    }

    return render(request, 'stardew/community_center.html', {
        'bundles': bundle_list,
        'tracker': tracker,
        'percent': tracker.percent_complete(bundle_list),
        'completed_bundle_ids': completed_bundle_ids,
    })

# view for handling post request to check or uncheck a single bundleitem
def toggle_item(request, item_id):
    # Only allow POST to prevent accidental toggling via a URL visit
    if request.method == 'POST':
        tracker = BundleTracker(request.session)

        # Make sure the item actually exists before toggling
        get_object_or_404(BundleItem, id=item_id)

        # Toggle donated state in the session
        tracker.toggle(item_id)

    return redirect('stardew:community_center')

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