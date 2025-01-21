from django.shortcuts import render
from .models import Home

def home(request):
    home = Home.objects.filter().first()
    return render(request, 'courses/home.html', { 'home': home})

# Create your views here.
