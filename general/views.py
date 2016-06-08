from django.shortcuts import render, redirect
from general import models
import random
from django.db import transaction
import haikunator

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

    items_print = models.items.objects.filter(item_type="print")
    context_dict['items_print'] = items_print

    items_art = models.items.objects.filter(item_type="art")
    context_dict['items_art'] = items_art

    items_clothing = models.items.objects.filter(item_type="clothing")
    context_dict['items_clothing'] = items_clothing

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

def new_room(request):
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = haikunator.haikunate()
            if models.Room.objects.filter(label=label).exists():
                continue
            new_room = models.Room.objects.create(label=label)
    return redirect('/general/chat_room', label=label)

def chat_room(request, label):
    room, created = models.Room.objects.get_or_create(label=label)

    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, 'room.html', {'room': room, 'messages': messages})
