# for a list of models filed types:
# https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        ("MEMBERSHIP_BRONZE", "Bronze"),
        ("MEMBERSHIP_SILVER", "Silver"),
        ("MEMBERSHIP_GOLD", "Gold"),
    ]
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True, max_length=155)
    phone = models.CharField(max_length=12)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
    )


class Order(models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETED = "C"
    PAYMENT_STATUS_FAILED = "F"

    PAYMENT_STATUSES = [
        ("PAYMENT_STATUS_PENDING", "Pending"),
        ("PAYMENT_STATUS_COMPLETED", "Completed"),
        ("PAYMENT_STATUS_FAILED", "Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUSES, default=PAYMENT_STATUS_PENDING
    )


class address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True
    )
