from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from Exam_project.accounts.forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm


def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user_profile.html', context)


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
