from django.shortcuts import render, redirect

from book.forms import BookForm
from book.models import BookModel


def index(request):
    context = {
        "books": BookModel.objects.all(),
    }
    return render(request, "index.html", context)


def create(request):
    if request.method == "GET":
        context = {
            "form": BookForm(),
        }
        return render(request, "create.html", context)

    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

        context = {
            "form": form,
        }
        return render(request, "create.html", context)


def edit(request, pk):
    book = BookModel.objects.get(pk=pk)

    if request.method == "GET":
        form = BookForm(instance=book)
        context = {
            "form": form,
        }
        return render(request, "edit.html", context)

    else:
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect("index")

        context = {
            "form": form,
        }
        return render(request, "edit.html", context)
