from django import forms

from motorbike_shop.models import Bikes


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bikes
        fields = "__all__"
