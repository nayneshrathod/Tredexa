from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    wight = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = 'ProductApp'
