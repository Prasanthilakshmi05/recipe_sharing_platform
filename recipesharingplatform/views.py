from django.shortcuts import render
from django.http import HttpResponse
from AllRecipes.models import User
from Tasty.models import User
from Yummly.models import Ingredient
from Cookpad.models import Ingredient
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,'index.html')
def AllRecipes(request):
    recipe = User.objects.all()
    return render(request, "AllRecipes.html" ,{'User': recipe})
def Tasty(request):
    objects= User.objects.all()
    return render(request, "Tasty.html" ,{'User': objects})
def Cookpad(request):
    cookpad= Ingredient.objects.all()
    return render(request, "Cookpad.html" ,{'Ingredient': cookpad})
def Yummly(request):
    yummy= Ingredient.objects.all()
    return render(request, "Yummly.html" ,{'Ingredient': yummy})
    
    