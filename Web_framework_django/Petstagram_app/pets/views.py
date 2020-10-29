from django.shortcuts import render, redirect

from pets.forms.comment_form import CommentForm
from pets.forms.pet_form import PetForm
from pets.models import Pet, Like, Comment


def pet_all(request):
    context = {
        "pets": Pet.objects.all
    }
    return render(request, "pet_list.html", context)


def detail_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == "GET":
        context = {
            "pet": pet,
            "form": CommentForm(),
        }
        return render(request, "pet_detail.html", context)

    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data["text"])
            comment.pet = pet
            comment.save()
            return redirect("pet detail or comment", pk)

        context = {
            "pet": pet,
            "form": form,
        }
        return render(request, "pet_detail.html", context)


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.save()
    return redirect("pet detail or comment", pk)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == "GET":
        context = {
            "form": PetForm(instance=pet),
            "pet": pet,
        }
        return render(request, "pet_edit.html", context)
    else:
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect("pet detail or comment", pk)

        context = {
            "form": form,
            "pet": pet,
        }
        return render(request, "pet_edit.html", context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            "pet": pet
            }
        return render(request, "pet_delete.html", context)
    else:
        pet.delete()
        return redirect("pets")


def create_pet(request):
    if request.method == "GET":
        form = PetForm()
        context = {
            "form": form,
        }
        return render(request, "pet_create.html", context)
    else:
        form = PetForm(request.POST)

        if form.is_valid():
            pet = form.save()
            return redirect("pet detail or comment", pet.pk)
        context = {
            "form": form
        }
        return render(request, "pet_list.html", context)
