from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from motorbike_shop import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.BikesListView.as_view(), name="home page"),
]

urlpatterns += staticfiles_urlpatterns()

