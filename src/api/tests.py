from rest_framework import status
from django.contrib.auth.models import User
from django.test import TestCase, Client
from api.helper import decrypt_data, encrypt_data
from api.models import FullCard


client = Client()


class HyperAtivaAPITest(TestCase):
    """ Test module for API """

    def setUp(self):
        self.API_URL = "/api/"
        self.API_TOKEN_URL = "/token/"
        self.create_user()
        self.token = self.get_auth_token()
        self.card = self.create_card_for_test()
        self.headers = {"Authorization": "Bearer {token}".format(token=self.token)}

    def create_user(self):
        user = User(username="test", is_active=True)
        user.set_password("test123")
        user.save()
        return user

    def get_auth_token(self):
        response = client.post(self.API_TOKEN_URL, data={"username": "test", "password": "test123"})
        return response.data.get("access")

    def create_card_for_test(self):
        card_number = encrypt_data("1234567890")
        obj = FullCard.objects.create(card_number=card_number)
        return obj

    def test_get_card_no_credencials_provided(self):
        data = {"card_number": "1234567890"}
        response = client.get(self.API_URL, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_card(self):
        data = {"card_number": "1234567890"}
        response = client.get(self.API_URL, data=data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data.get("card_number"), decrypt_data(self.card.card_number))

    def test_get_invalid_card(self):
        data = {"card_number": "12345678901"}
        response = client.get(self.API_URL, data=data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
