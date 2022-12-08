from django import forms
from django.utils import timezone


class SearchForm(forms.Form):
    identity = forms.CharField(max_length=50, required=False)
    STATUS_CHOICES = [
        ('', ''),
        ('н', 'Не активирована'),
        ('а', 'Активирована'),
        ('п', 'Просрочена'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, initial='')
    series = forms.CharField(required=False, max_length=50)
    date_of_issue = forms.DateTimeField(required=False)
    valid_thru = forms.DateTimeField(required=False, initial=timezone.now())
    
    
class CreateCardForm(forms.Form):
    series = forms.CharField(required=True, max_length=50)
    count = forms.IntegerField(required=True)
    STATUS_CHOICES = [
        ('1', '1 месяц'),
        ('6', '6 месяцев'),
        ('12', '1 год'),
    ]
    valid_thru = forms.ChoiceField(choices=STATUS_CHOICES, required=False, initial='')
    
