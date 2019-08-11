from django.conf.urls import *
from django.contrib import admin
from django.views.generic import ListView, DetailView

from . import views
from .models import Rider, Country


class NationRiders(ListView):
    model = Rider
    context_object_name = "riders"
    template_name = "Cycl/nation_riders.html"

    def get_queryset(self):
        return Rider.objects.filter(nation__name=self.kwargs['name'])

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(NationRiders, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories, sans filtre particulier
        context['nations'] = Country.objects.all()
        return context


class ViewRider(DetailView):
        context_object_name = "rider"
        model = Rider
        template_name = "Cycl/view_rider.html"


urlpatterns = [
    url(r'^nation/(?P<name>.+)',
        NationRiders.as_view(model=Rider,
                             context_object_name="riders"),
        name="nation_riders"),
    url(r'^rider/(?P<pk>\d+)$', ViewRider.as_view(),
        name='view_rider'),
]
