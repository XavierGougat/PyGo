from django.contrib import admin
from django.conf.urls import url
from blog import views
from django.views.generic import ListView

urlpatterns = [
    url(r'^categorie/(?P<id>\d+)', views.ListeArticles.as_view(), name="blog_categorie"),
    url(r'^article/(?P<pk>\d+)$', views.LireArticle.as_view(), name='blog_lire'),
]