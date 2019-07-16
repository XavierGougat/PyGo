from django.shortcuts import render
from django.http import HttpResponse, Http404

def view_article(request, id_article):

    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)    
    )