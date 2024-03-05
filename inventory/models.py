from django.db import models


class Establishment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    locations = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=100)
    objects = models.Manager()  # явное указание атрибута objects

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'establishments'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    objects = models.Manager()  # явное указание атрибута objects

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'products'
