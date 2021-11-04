from rest_framework import status
from api.src.authentication.tests.base_test import BaseTest

class ProductsTests(BaseTest):
    
    def test_can_creat_product(self):
        data = {
            "name": "Delmonte",
            "price": 205.00
        }
        res= self.client.post(self.PRODUCT_CREATE_URL,
        data,HTTP_AUTHORIZATION=self.access_token,format="json")
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
    

    def test_can_get_all_products(self):
        res= self.client.get(self.PRODUCT_LIST_URL,format="json")
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        

    def test_can_get_one_products(self):
        data1 = {
            "name": "Fanta",
            "price": 50.00
        }
        res = self.client.post(self.PRODUCT_CREATE_URL,
        data1,HTTP_AUTHORIZATION=self.access_token,format="json")
        res1= self.client.get(self.PRODUCT_RETRIEVE_URL+str(res.data['id'])+"/", format="json")
        self.assertEqual(res1.status_code,status.HTTP_200_OK)
