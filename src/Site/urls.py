from django.contrib import admin
from django.urls import path
from .views import accueil

urlpatterns = [
   path('index/', accueil, name='index'),
]
