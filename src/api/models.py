from django.db import models

from api.helper import decrypt_data, encrypt_data

class FullCard(models.Model):
    card_number = models.CharField(max_length=256)
    batch_date = models.DateField(null=True, blank=True)
    batch_number = models.CharField(max_length=8, null=True, blank=True)
    sequential_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.get_card_info()
    
    def set_card_info(self, card_number):
        self.card_number = encrypt_data(card_number)

    def get_card_info(self):
        card_number = decrypt_data(self.card_number)
        return card_number

    class Meta:
        app_label = "api"
