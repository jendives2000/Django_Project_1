# for a list of models filed types:
# https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)


class 