from django.views.generic import ListView, DeleteView, CreateView
from django.shortcuts import render, HttpResponse

from App.forms import AjoutForm
from .models import projet
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    return HttpResponse("Bonjour a tous")


def home(req, up):
    return HttpResponse("bonjour UP "+up)
    # return HttpResponse(f"bonjour UP {up}")


def affiche(req):
    projects = projet.objects.all()
    dump = print(projects)
    resultat = "------".join(p.nom_projet for p in projects)
    # return HttpResponse(resultat, dump)
    return render(req, 'App/affiche.html', {'pp': projects})


class afficheLV(ListView):
    model = projet
    template_name = "App/Affiche.html"
    context_object_name = 'pp'
    ordering = ['-nom_projet']
# - pour des ou asc


class Delete(DeleteView):
    model = projet
    success_url = reverse_lazy('AFF')


class projetCreateView(CreateView):
    model = projet
    # template_name = "App/ajout.html"
    # fields = ["nom_projet", "duree_projet", "createur", "temps_alloue", "suprviseur"]
    # fields = '__all__'
    form_class = AjoutForm
    success_url = reverse_lazy('AFF')
