from django.shortcuts import render,redirect
from .form import RecipeForm

def Recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AllRecipes')  
        form = RecipeForm()
    return render(request, 'Recipe_form.html', {'form': form})
# Create your views here.
