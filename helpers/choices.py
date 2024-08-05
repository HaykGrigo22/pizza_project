from django.db import models


class ThickTypeChoice(models.TextChoices):
    type1 = "classic", "Classic"
    type2 = "thin", "Thin"
    type3 = "thick", "Thick"
    type4 = "california style", "California Style"
    type5 = "detroit style", " Detroit Style"


class RateChoice(models.TextChoices):
    type1 = "★★★★★", "★★★★★"
    type2 = "★★★★☆", "★★★★☆"
    type3 = "★★★☆☆", "★★★☆☆"
    type4 = "★★☆☆☆", "★★☆☆☆"
    type5 = "★☆☆☆☆", "★☆☆☆☆"
