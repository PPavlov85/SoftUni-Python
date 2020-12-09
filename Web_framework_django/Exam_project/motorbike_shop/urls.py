from django.urls import path
from motorbike_shop import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from motorbike_shop.views import send_email

urlpatterns = [
    path('', views.BikesListView.as_view(), name="home page"),
    path('details/<int:pk>/', views.BikeDetailsView.as_view(), name="bike details"),
    path('add/', views.BikeAddView.as_view(), name="bike add"),
    path('update/<int:pk>/', views.BikeUpdateView.as_view(), name="bike update"),
    path('delete/<int:pk>/', views.BikeDeleteView.as_view(), name="bike delete"),
    path('send_email/', send_email, name="send email"),
]
