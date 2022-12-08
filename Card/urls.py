from django.urls import path
from Card.views import MainPage, tools, CreatePage



urlpatterns = [
    path('<str:identity>/<str:key>', tools, name='main'),
    path('create/', CreatePage, name='create'),
    path('', MainPage, name='main'),
]