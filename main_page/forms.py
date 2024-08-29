from django import forms
from django.forms import inlineformset_factory

from burger.forms import AddBurger
from burger.models import Burger
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


PizzaFormSet = inlineformset_factory(Producers, Pizzas, form=AddPizza, fields='__all__', extra=1)
BurgerFormSet = inlineformset_factory(Producers, Burger, form=AddBurger, fields='__all__', extra=1)

