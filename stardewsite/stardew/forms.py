from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Season, FarmingItem, ForagingItem, FishingItem
# Form is only created this way so I can show mastery - Ideally this app will deal with checkboxes more than real form input
# This is a temp solution for that until I get the other aspects of the game in the app
# class CropForm(forms.ModelForm):
#     class Meta:
#         model = Crop
#         fields = ['name', 'season', 'growth_time', 'sell_price']

# Login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Registration form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput,
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

    # Methods
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password don't match.")
        return cd['password']