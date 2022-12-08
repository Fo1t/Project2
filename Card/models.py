from django.db import models
from datetime import timedelta
from django.utils import timezone



class Card(models.Model):
    identity = models.CharField(primary_key=True, max_length=100)
    STATUS_CHOICES = [
        ('н', 'Не активирована'),
        ('а', 'Активирована'),
        ('п', 'Просрочена'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                            default='с', blank=True)
    series = models.CharField(blank=True, default='', max_length=50)
    date_of_issue = models.DateTimeField(default=timezone.now())
    valid_thru = models.DateTimeField(blank=False, default=(timezone.now()+timedelta(days=30)))
    sum = models.IntegerField(default=0)
    
