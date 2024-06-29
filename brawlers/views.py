from django.shortcuts import render
from .models import Brawler
import random

def home(request):
    brawlers = Brawler.objects.all()
    context = {
        'brawlers': brawlers
    }
    return render(request, 'home.html', context)

def random_brawler_view(request):
    brawlers = Brawler.objects.all()
    random_brawler = random.choice(brawlers)
    context = {
        'random_brawler': random_brawler
    }
    return render(request, 'random_brawler.html', context)
