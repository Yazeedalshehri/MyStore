from django.test import TestCase
from base.models import *



class TestModels(TestCase):

    def test_admin_register(self):
       
        self.Admin1 = Admins.objects.create(

            username = "hatan"
            , email= "Hatan@gmail.com"
            , password= "Hatan12544"
            , phonenumber= "0555325629"
            , storename= "HatanStore"
            , category= "HatanCategory"
            , storecolor= "#2255d"
            , StoreTextColor= "#2255d"
            , StoreBackgroundColor= "#2255d"
            , totalprice= 2.99
            , slug = "hatan"
            , storeEmail= "HatanStore@gmail.com"
            , StorePhone= "0555325629"
        )
       
        self.assertEqual(self.Admin1.slug , "hatan")    

    

