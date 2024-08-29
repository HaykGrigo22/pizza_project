from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from helpers.choices import ThickTypeChoice, RateChoice
from helpers.validators import valid_price
from helpers.storage import upload_pizza_image, upload_producer_logo_image


class Producers(models.Model):
    producer_name = models.CharField(max_length=155)
    description = models.TextField()
    rate = models.CharField(max_length=155, choices=RateChoice.choices)
    logo = models.ImageField(upload_to=upload_producer_logo_image, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("producer", kwargs={"pk": self.pk})

    def __str__(self):
        return self.producer_name

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"


class Pizzas(models.Model):
    title = models.CharField(max_length=50)
    producer = models.ForeignKey(Producers, on_delete=models.CASCADE, null=True, blank=True, related_name="pizzas")
    price = models.PositiveIntegerField(validators=[valid_price])
    description = models.TextField()
    rate = models.CharField(max_length=155, choices=RateChoice.choices, default="6.0")
    thick_type = models.CharField(max_length=155, choices=ThickTypeChoice.choices, default="classic")
    image = models.ImageField(upload_to=upload_pizza_image, null=True, blank=True)

    def __str__(self):
        return f"Pizza -> {self.title}"

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"
