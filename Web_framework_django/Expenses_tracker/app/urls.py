from django.urls import path
from app.views.index import index
from app.views.expenses import create_expense, edit_expense, delete_expense
from app.views.profiles import index_profile, delete_profile, create_profile, edit_profile

urlpatterns = [
    path('', index, name="index"),
    path('create/', create_expense, name="create expense"),
    path('edit/<int:pk>/', edit_expense, name="edit expense"),
    path('delete/<int:pk>/', delete_expense, name="delete expense"),
    path('profile/', index_profile, name="index profile"),
    path('profile/create/', create_profile, name="create profile"),
    path('profile/edit/', edit_profile, name="edit profile"),
    path('profile/delete/', delete_profile, name="delete profile"),
]
