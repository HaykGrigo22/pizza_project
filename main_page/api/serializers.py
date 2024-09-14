from rest_framework import serializers

from main_page.models import Pizzas


class PizzaSerializer(serializers.Serializer):

    class Meta:
        model = Pizzas
        fields = ("title", "producer", "price", "rate", "image")


class BurgerSerializer(serializers.Serializer):
    class Meta:
        model = Pizzas
        fields = ("title", "producer", "price", "rate", "image")


class ProducerSerializer(serializers.Serializer):
    class Meta:
        model = Pizzas
        fields = ("producer_name", "rate", "creator", "logo")
