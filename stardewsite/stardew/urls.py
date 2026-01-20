from django.urls import path
from . import views

app_name = 'stardew'
# Defining the url pattern for the app 
urlpatterns = [
    # path for the crops
    path('crops/', views.crop_list, name='crop_list'),
]