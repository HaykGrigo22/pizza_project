from django import forms
from burger.models import *


class AddBurger(forms.ModelForm):

    class Meta:
        model = Burger
        fields = ["title", "producer", "price", "description", "rate", "image"]
        widgets = {
            "description": forms.Textarea()
        }
