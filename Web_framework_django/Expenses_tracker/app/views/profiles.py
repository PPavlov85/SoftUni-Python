from django.shortcuts import render, redirect

from app.common.budget import calculate_budget_left
from app.forms.profiles import ProfileForm
from app.models import Profile, Expenses


def index_profile(request):
    expenses = Expenses.objects.all()
    profile = Profile.objects.all()[0]

    profile.budget_left = calculate_budget_left(profile, expenses)

    context = {
        "profile": profile,
    }
    return render(request, "profile.html", context)


def create_profile(request):
    if request.method == "GET":
        context = {
            "form": ProfileForm(),
        }
        return render(request, "home-no-profile.html", context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        context = {
            "form": form,
        }
        return render(request, "home-no-profile.html", context)


def edit_profile(request):
    profile = Profile.objects.all()[0]

    if request.method == "GET":
        context = {
            "form": ProfileForm(instance=profile),
        }
        return render(request, "profile-edit.html", context)

    else:
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("index profile")

        context = {
            "form": form,
        }
        return render(request, "profile-edit.html", context)


def delete_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == "GET":
        return render(request, "profile-delete.html")
    else:
        profile.delete()
        Expenses.objects.all().delete()
        return redirect("index")
