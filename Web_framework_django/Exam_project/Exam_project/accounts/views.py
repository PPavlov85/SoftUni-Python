from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views.generic.base import View

from Exam_project.accounts.forms import UserProfileForm, RegisterUserForm
from Exam_project.accounts.models import Profile


def profile(request):
    context = {
        "u_form": RegisterUserForm(instance=request.user),
        "p_form": UserProfileForm(instance=request.user.profile),
    }
    return render(request, "user_profile.html", context)


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login user')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


class LoginUserView(LoginView):
    template_name = "login_user.html"
