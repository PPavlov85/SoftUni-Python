from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models


class BikesListView(ListView):
     context_object_name = "bikes"
     model = models.Bikes
     template_name = "index.html"
