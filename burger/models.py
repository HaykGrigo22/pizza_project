from django.db import models
from django.urls import reverse

from helpers.choices import RateChoice
from helpers.storage import upload_burger_image
from helpers.validators import valid_price
from main_page.models import Producers


class Burger(models.Model):
    title = models.CharField(max_length=50)
    producer = models.ForeignKey(Producers, on_delete=models.CASCADE, null=True, blank=True, related_name="burger")
    price = models.PositiveIntegerField(validators=[valid_price])
    description = models.TextField()
    rate = models.CharField(max_length=155, choices=RateChoice.choices, default="6.0")
    image = models.ImageField(upload_to=upload_burger_image, null=True, blank=True)

    def __str__(self):
        return f"{self.title} Burger"

    def get_absolute_url(self):
        return reverse("burger", kwargs={"pk": self.pk})
