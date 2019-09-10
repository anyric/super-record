from django.db import models
from accounts.models import User

class Product(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=100,unique=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.FloatField(verbose_name='unit price')
    stock_level = models.PositiveIntegerField(verbose_name='stock level')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of this Product."""
        return self.name