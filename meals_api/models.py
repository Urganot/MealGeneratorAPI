from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=255)
    chefkoch_slug = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_chefkoch_url(self):
        return "https://www.chefkoch.de/rezepte/" + self.chefkoch_slug
