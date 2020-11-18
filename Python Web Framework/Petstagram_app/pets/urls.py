from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Petstagram_app.view import index
from pets.views import pet_all, detail_or_comment_pet, pet_like, edit_pet, delete_pet, create_pet

urlpatterns = [
    path('', index, name="index"),
    path("pets/", pet_all, name="pets"),
    path("pets/details/<int:pk>/", detail_or_comment_pet, name="pet detail or comment"),
    path("pets/like/<int:pk>/", pet_like, name="pet like"),
    path("pets/edit/<int:pk>/", edit_pet, name="edit pet"),
    path("pets/delete/<int:pk>/", delete_pet, name="delete pet"),
    path("pets/create/", create_pet, name="create pet")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
