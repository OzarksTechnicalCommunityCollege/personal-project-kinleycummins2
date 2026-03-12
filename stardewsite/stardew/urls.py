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

    # Temporaily removed, form is not yet fixed with new models 
    # path('crops/add/', views.add_crop, name='add-crop'),
]