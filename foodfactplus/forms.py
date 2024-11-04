# forms.py
from django import forms

class RecipeForm(forms.Form):
    name = forms.CharField(label='Recipe Name', max_length=100)
    food_items = forms.CharField(label='Food Items (comma-separated)', widget=forms.Textarea)
