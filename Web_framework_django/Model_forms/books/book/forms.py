from django import forms
from book.models import BookModel


class BookForm(forms.ModelForm):

    def clean_pages(self):
        pages = self.cleaned_data["pages"]
        if pages <= 0:
            raise ValueError("Pages should be positive number")
        return pages

    class Meta:
        model = BookModel
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "pages": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control"
                }
            ),
        }
