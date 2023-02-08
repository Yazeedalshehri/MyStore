from django.test import TestCase, Client
from django.urls import reverse
from base.views import *


class Testviews(TestCase):
    
    def test_HomePage_view(self):
        clinet = Client()

        response = clinet.get(reverse('homepage'))

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'HomePage.html')

    