from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from Exam_project.accounts.views import register, profile

urlpatterns = [
    # path("profile/<int:pk>", UserProfileView.as_view(), name="user profile"),
    path('profile/', profile, name="profile"),
    path("register/", register, name="register user"),
    path('login/', LoginView.as_view(template_name='login_user.html'), name='login user'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout user'),
]
