from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    image  = models.FileField()

    def get_absolute_url(self):
        return reverse('myapp:productdetail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + ' - ' + self.price
