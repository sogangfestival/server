from django.db import models

class Building(models.Model):
    building_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.building_name