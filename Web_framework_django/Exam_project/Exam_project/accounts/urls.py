from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from Exam_project.accounts.views import register, profile

urlpatterns = [
    path('accounts/change-password/', PasswordChangeView.as_view(template_name='change-password.html'),
         name="change_password"),
    path('accounts/change-password-done/', PasswordChangeDoneView.as_view(template_name='change-password-done.html'),
         name="password_change_done"),
    path('profile/', profile, name="profile"),
    path("register/", register, name="register user"),
    path('login/', LoginView.as_view(template_name='login_user.html'), name='login user'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout user'),
]
