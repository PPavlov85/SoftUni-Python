from django.urls import path

from app.views.views import index, details, create, edit, delete

urlpatterns = [
    path("", index, name="home page"),
    path("create/", create, name="create recipe"),
    path("edit/<int:pk>/", edit, name="edit recipe"),
    path("delete/<int:pk>/", delete, name="delete recipe"),
    path("details/<int:pk>/", details, name="details recipe"),
]
