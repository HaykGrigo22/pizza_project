from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from burger.models import Burger
from main_page.api.serializers import PizzaSerializer, BurgerSerializer, ProducerSerializer
from main_page.models import Pizzas, Producers


@api_view(["GET"])
def get_pizza_list(request):
    all_pizzas = Pizzas.objects.all()
    serializer = PizzaSerializer(all_pizzas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_burger_list(request):
    all_burgers = Burger.objects.all()
    serializer = BurgerSerializer(all_burgers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_producer_list(request):
    all_producers = Producers.objects.all()
    serializer = ProducerSerializer(all_producers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
