from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Bikes


class BikesListView(ListView):
    template_name = "index.html"
    context_object_name = "bikes"
    model = models.Bikes
    paginate_by = 12
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BikeDetailsView(DetailView):
    model = Bikes
    template_name = "details_bike.html"
    context_object_name = "bike"


class BikeUpdateView(UpdateView):
    model = Bikes
    template_name = "update_bike.html"
    fields = "__all__"
    success_url = reverse_lazy("home page")


class BikeAddView(CreateView):
    model = Bikes
    template_name = "add_bike.html"
    fields = "__all__"
    success_url = reverse_lazy("home page")


class BikeDeleteView(DeleteView):
    model = Bikes
    fields = "__all__"
    template_name = "delete_bike.html"
    success_url = reverse_lazy("home page")


def send_email(request):
    if request.method == "POST":

        template = render_to_string("email/email_template.html", {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "message": request.POST["message"],
        })

        email = EmailMessage(
            request.POST["subject"],
            template,
            settings.EMAIL_HOST_USER,
            ["pavlov85pavel@gmail.com"],
        )
        email.fail_silently = False
        email.send()

    return render(request, "email/email_sent.html")
