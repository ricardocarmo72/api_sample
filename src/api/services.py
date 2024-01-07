from datetime import datetime

from django.db import transaction

from api.helper import encrypt_data
from api.models import FullCard


class FullCardService:

    def find_card(self, card_number):
        card_number = encrypt_data(card_number)
        return FullCard.objects.filter(card_number=card_number).first()
    
    @transaction.atomic
    def insert(self, card_number):
        card_number = encrypt_data(card_number)
        obj = FullCard.objects.create(card_number=card_number)
        return obj

    @transaction.atomic
    def bulk_insert(self, data):
        header = data[0].decode('utf-8')
        batch_date = datetime.strptime(header[29:37], '%Y%m%d')
        batch_number = header[37:45].strip()
        card_count = int(header[45:51])

        cards = []
        for i in range(1, card_count + 1):
            line = data[i].decode('utf-8')
            sequential_number = int(line[1:7].strip())
            card_number = line[7:26].strip()
            card_number = encrypt_data(card_number)
            cards.append(FullCard(
                batch_number=batch_number,
                sequential_number=sequential_number,
                card_number=card_number,
                batch_date=batch_date
                )
            )
        objs = FullCard.objects.bulk_create(cards)
        return objs
