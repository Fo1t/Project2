from django.db import models
from Card.models import Card


class Order(models.Model):
    card = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL)
    
        

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    price = models.PositiveIntegerField()
