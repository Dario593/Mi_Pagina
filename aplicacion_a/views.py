from django.shortcuts import render

from .models import Musica
from .models import Principal


def home(request):
    musicas = Musica.objects.all()
    return render(request, 'home.html', {'musicas': musicas})


def base(request):
    principals = Principal.objects.all()
    return render(request, 'base.html', {'principals': principals})

