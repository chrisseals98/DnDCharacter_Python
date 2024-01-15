from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Character

# Create your views here.
class ListView(generic.ListView):
    model = Character
    template_name = "list.html"
    context_object_name = "characters"
    
class DetailedView(generic.DetailView):
    model = Character
    template_name = "detailed.html"
    context_object_name = "character"