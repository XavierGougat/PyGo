from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('article/<int:id_article>', views.view_article),
]