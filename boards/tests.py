from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve
from django.urls import resolve
from django.test import TestCase
from .views import home



class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    def test_home_url_resolvers_home_view(self):
        view =resolve('/homePage/')
        self.assertEqual(view.func,home)
