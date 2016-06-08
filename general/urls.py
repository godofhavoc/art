from django.conf.urls import patterns, include, url
from django.contrib import admin
from general import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^space/$', views.space, name='space'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]
