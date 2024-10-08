from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.model}"


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Individual Entrepreneur'),
    ]

    name = models.CharField(max_length=255)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, blank=True)
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='clients')
    debt = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.00)], null=True,
                               blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.supplier:
            if self.level != self.supplier.level + 1:
                raise ValidationError("The level of the supplier should be one less than the level of the client")
        else:
            if self.level != 0:
                raise ValidationError("Only factories(level 0) can have suppliers")
