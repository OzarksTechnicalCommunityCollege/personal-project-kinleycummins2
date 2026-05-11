from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
import debug_toolbar

app_name = 'stardew'
# Defining the url pattern for the app 
urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # path for the crops
    path('seasons/', views.season_list, name='season-list'),

    # Login/Logout views
    path('login/', auth_views.LoginView.as_view(template_name='stardew/registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='stardew/registration/logged_out.html'),name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),

    # debug toolbar
    path('__debug__/', include(debug_toolbar.urls)),

    # displays the full community center checklist
    path('community-center/', views.community_center, name='community_center'),

    # handles checkbox toggle for a single bundle item (POST only)
    path('community-center/toggle/<int:item_id>/', views.toggle_item, name='toggle_item'),

    # MODULE 8 URL PATH 
    path("weather/", views.weather_view, name="weather"),

]