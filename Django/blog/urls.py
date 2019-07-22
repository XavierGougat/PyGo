from django.contrib import admin
from django.conf.urls import url
from blog import views
from django.views.generic import ListView

urlpatterns = [
    url(r'^categorie/(\d+)$', views.ListeArticles.as_view(), name="blog_categorie"),
]