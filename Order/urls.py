from django.urls import path
from Order.views import OrderPage


urlpatterns = [
    path('<str:card_identity>', OrderPage, name='order'),
]