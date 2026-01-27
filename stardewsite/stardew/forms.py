from django import forms
from .models import Crop
# Form is only created this way so I can show mastery - Ideally this app will deal with checkboxes more than real form input
# This is a temp solution for that until I get the other aspects of the game in the app
class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'season', 'growth_time', 'sell_price']