import json

from rest_framework.test import APIClient
from django.test import TestCase
from api.src.authentication.models import User
from api.src.authentication.serializer import RegisterSerializer


class BaseTest(TestCase):

    def setUp(self):

        self.LOGIN_URL = '/api/v1/auth/login/'
        self.REGISTER_URL = '/api/v1/auth/register/'
        self.PRODUCT_LIST_URL='/api/v1/products/product/'
        self.PRODUCT_RETRIEVE_URL='/api/v1/products/product/'
        self.PRODUCT_CREATE_URL='/api/v1/products/product/'



        self.test_user1 = {
                "username": "admin",
                "email": "admin@gmail.com",
                "role": 1,
                "password": "1234"
            }

        self.test_user2 = {
            'username':'manager',
            'email':'manager@gmail.com',
            'role': 2,
            'password':'1234'
        }

        self.test_user3 = {
            'username':'cashier',
            'email':'cashier@gmail.com',
            'role': 3,
            'password':'1234'
        }

        self.new_user = {
            'username':'shop',
            'email':'shop@gmail.com',
            'role': 3,
            'password':'1234'
        }
        super_admin = RegisterSerializer(data=self.test_user1)
        super_admin.is_valid()
        super_admin.save()
        

        self.client = APIClient()
        res = self.client.post(self.LOGIN_URL, self.test_user1, format="json")
        self.access_token = "Bearer " + eval(res.data['tokens'])['access']
