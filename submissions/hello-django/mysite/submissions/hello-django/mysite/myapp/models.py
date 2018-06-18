from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Armoury(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name