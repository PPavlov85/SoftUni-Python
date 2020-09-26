from django.contrib import admin
from django.urls import path
from first_django_project_2.views import UsersClassView, GamesListView, index

urlpatterns = [
    path('', index),
    path("2/", UsersClassView.as_view()),
    path("games/", GamesListView.as_view()),
    path('admin/', admin.site.urls)
]
