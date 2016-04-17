from django.shortcuts import render
from general import models

# Create your views here.
def index(request):
    context_dict = {}
    context_dict['nbar'] = 'home'
    return render(request, 'index.html', context_dict)

def artists(request):
    context_dict = {}
    context_dict['nbar'] = 'artists'

    artists = models.artists.objects.all()
    context_dict['artists'] = artists

    return render(request, 'artists.html', context_dict)

def shop(request):
    context_dict = {}
    context_dict['nbar'] = 'shop'
    return render(request, 'shop.html', context_dict)

def about(request):
    context_dict = {}
    context_dict['nbar'] = 'about'
    return render(request, 'about.html', context_dict)

def gallery(request):
    context_dict = {}
    context_dict['nbar'] = 'gallery'
    return render(request, 'gallery.html', context_dict)

def space(request):
    context_dict = {}
    context_dict['nbar'] = 'space'
    return render(request, 'space.html', context_dict)
