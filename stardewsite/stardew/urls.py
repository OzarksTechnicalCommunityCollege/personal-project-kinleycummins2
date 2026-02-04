from django.urls import path
from . import views

app_name = 'stardew'
# Defining the url pattern for the app 
urlpatterns = [
    # path for the crops
    path('seasons/', views.season_list, name='season-list'),
    # Temporaily removed, form is not yet fixed with new models 
    # path('crops/add/', views.add_crop, name='add-crop'),
]