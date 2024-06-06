from django.shortcuts import render
from django.http import HttpResponse
from AllRecipes.models import Recipe
from Tasty.models import User
from Yummly.models import Yummy
from Cookpad.models import Ingredient
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request,'index.html')
@login_required
def AllRecipes(request):
    recipe = Recipe.objects.all()
    return render(request, "AllRecipes.html" ,{'Recipe':recipe})

@login_required
def Tasty(request):
    variety = User.objects.all()
    return render(request, "Tasty.html" ,{'User': variety})
@login_required
def Cookpad(request):
    cookpad = Ingredient.objects.all()
    return render(request, "Cookpad.html" ,{'Ingredient': cookpad})
@login_required
def Yummly(request):
    yummy = Yummy.objects.all()
    return render(request, "Yummly.html" ,{'Yummy': yummy})
    
@login_required
def forms(request):
    # Your view logic here
    return render(request, 'Recipe_form.html')