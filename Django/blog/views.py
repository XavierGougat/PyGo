from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from .models import Article, Categorie

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

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ListeArticles, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories, sans filtre particulier
        context['categories'] = Categorie.objects.all()
        return context

class LireArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/lire.html"