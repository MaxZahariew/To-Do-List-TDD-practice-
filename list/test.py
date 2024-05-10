from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve

from list.views import home_page


# Create your tests here.
class TestHomePage(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>To Do</title>', html)