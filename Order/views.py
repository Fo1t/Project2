from django.shortcuts import render
from Order.models import Order, Item
from Card.models import Card



def OrderPage(request, card_identity=None):
    data = {}
    if Card.objects.filter(identity=card_identity).exists():
        card = Card.objects.get(identity=card_identity)
        orders = Order.objects.filter(card=card)
        answers = []
        for order in orders:
            items_info = ''
            for item in Item.objects.filter(order=order):
                items_info = items_info + f'{item.name} За {item.price} |'
            answers.append({
                'order': order,
                'items_info': items_info,
            })
        data['orders'] = answers
    
    return render(request, 'order.html', data)