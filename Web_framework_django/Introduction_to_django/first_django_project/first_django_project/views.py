from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView

# Same like ClassView

# def index(request):
#     title = "Dance studio New eX"
#     users = User.objects.all()
#     context = {
#         "title": title,
#         "users": users,
#     }
#     return render(request, "index.html", context)
#
from first_django_project.models import Game


class UsersClassView(ListView):
    model = User
    template_name = "index.html"


class GamesListView(ListView):
    model = Game
    template_name = "games.html"
