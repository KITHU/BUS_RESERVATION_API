import json
from rest_framework import status
from .base_test import BaseTest



class TestAuthUser(BaseTest):

    def test_user_registration(self):
        res = self.client.post(self.REGISTER_URL, self.test_user2, 
        HTTP_AUTHORIZATION=self.access_token,format="json")
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        self.assertEqual(res.data['username'], self.test_user2["username"])


    def test_user_login(self):
        res = self.client.post(self.REGISTER_URL, self.test_user2, 
        HTTP_AUTHORIZATION=self.access_token,format="json")
        res = self.client.post(self.LOGIN_URL, self.test_user2, format="json")
        self.assertEqual(res.status_code,status.HTTP_200_OK)
