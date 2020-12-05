from django.urls import path
from motorbike_shop import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from motorbike_shop.views import send_email

urlpatterns = [
    path('', views.BikesListView.as_view(), name="home page"),
    path('send_email/', send_email, name="send email")

]

urlpatterns += staticfiles_urlpatterns()
