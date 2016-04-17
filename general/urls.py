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
]
