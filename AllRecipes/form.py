from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
         model = Recipe
         fields = ['bio']
         widgets = {
             'Recipe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User_id name'}),
            
}