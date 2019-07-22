from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from .models import Article

def view_article(request, id_article):

    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)    
    )    

class ListeArticles(ListView):
    model = Article
    context_object_name = 'les_articles'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.filter(categorie__id=self.kwargs['id'])

