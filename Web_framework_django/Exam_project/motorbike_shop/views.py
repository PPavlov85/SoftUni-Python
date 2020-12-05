from django.shortcuts import render
from django.views.generic import ListView
from . import models
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


class BikesListView(ListView):
    template_name = "index.html"
    context_object_name = "bikes"
    model = models.Bikes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





def send_email(request):
    if request.method == "POST":

        template = render_to_string("email_template.html", {
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

    return render(request, "email_sent.html")
