from django.apps import AppConfig
import time
import threading
from django.conf import settings


def card_check_loop_thread():
    from Card.models import Card
    from django.utils import timezone
    while True:
        time.sleep(settings.CARD_UPDATE_SECOND)
        for card in Card.objects.filter(status='а'):
            if card.valid_thru < timezone.now():
                card.status = 'п'
                card.save()
        for card in Card.objects.filter(status='н'):
            if card.valid_thru < timezone.now():
                card.status = 'п'
                card.save()
        time.sleep(settings.CARD_UPDATE_SECOND)




class CardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Card'
    def ready(self):
        threading.Thread(target=card_check_loop_thread).start()
        
