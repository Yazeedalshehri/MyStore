from django.test import TestCase
from django.urls import reverse , resolve
from  base.views import  *

class TestUrls(TestCase):

    def test_HomePage_Url(self):
        url = reverse('homepage')
        self.assertEqual(resolve(url).func, HomePage)


    def test_register_Url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, Register)  

    def test_login_Url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, Login)   

    # Slug 
    def test_AdminPage_Url(self):
        url = reverse('AdminPage', args=['Slug'])
        self.assertEqual(resolve(url).func, AdminPage)   

    def test_Analytics_Url(self):
        url = reverse('Analytics', args=['Slug'])
        self.assertEqual(resolve(url).func, Analytics)   

    def test_Customers_Url(self):
        url = reverse('Customers', args=['Slug'])
        self.assertEqual(resolve(url).func, Customers)   

    def test_Products_Url(self):
        url = reverse('Products', args=['Slug'])
        self.assertEqual(resolve(url).func, Products)   

    def test_Orders_Url(self):
        url = reverse('Orders', args=['Slug'])
        self.assertEqual(resolve(url).func, Orders)   



