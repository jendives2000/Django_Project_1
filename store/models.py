# for a list of models filed types:
# https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types

from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    # !! DEPENDENCY -- 1 -- : 1toM !!:
    title = models.CharField(max_length=255)
    description = models.TextField()
    # CIRCULAR DEPENDENCY: MtoM !! :
    # put the dependee in "":
    # !!! dependee is now HARD CODED (if its class name changes, it wont be updated accordingly)
    featured_product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",  # prevents creation of an additional collection reverse relationship in class Product.
    )


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    # max_digits = num of digits before decimals.
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    # !! DEPENDENCY -- 1 -- : Mto1 !!:
    # Deleting a collection SHOULD NOT delete all its products
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion, related_name="promoted_products")


# NEEDS to be placed before class Order
class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True, max_length=155)
    phone = models.CharField(max_length=12)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_BRONZE,
    )

    class Meta:
        db_tables = "store_customers"
        indexes = [models.Index(fields=["last_name", "first_name"])]


class Order(models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETED = "C"
    PAYMENT_STATUS_FAILED = "F"

    PAYMENT_STATUSES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETED, "Completed"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUSES, default=PAYMENT_STATUS_PENDING
    )
    # NEVER delete orders from the database, hence the PROTECT method on_delete
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address(models.Model):
    zip = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderItem(models.Model):
    # Deleting an order WILL NOT delete its OrderItems
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    # this stores the price at order time. Product price can vary so we use this one for Orderitem.
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    title = models.CharField(max_length=255)
    description = models.TextField()
    added_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
