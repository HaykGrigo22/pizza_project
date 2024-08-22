from django import forms
from main_page.models import *


class AddPizza(forms.ModelForm):

    class Meta:
        model = Pizzas
        fields = ["title", "producer", "price", "description", "rate", "thick_type", "image"]
        widgets = {
            "description": forms.Textarea
        }


class AddProducer(forms.ModelForm):

    class Meta:
        model = Producers
        fields = ["producer_name", "description", "rate", "logo"]
        widgets = {
            "description": forms.Textarea(attrs={"placeholder": "some placeholder"})
        }
