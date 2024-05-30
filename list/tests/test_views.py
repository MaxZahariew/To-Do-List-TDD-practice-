from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve

from list.views import home_page
from list.models import Item


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        response = self.client.get('/')
        self.assertEqual(found.func, home_page)
        self.assertTemplateUsed(response, "main.html")

    def test_home_page_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf-8')
        self.assertIn('<title>To Do</title>', html)

    def test_can_save_a_POST_request(self):
        ''' Тест: можно сохранить post-запрос '''
        response = self.client.post('/', data={'item_text': 'A new list item'})
        html = response.content.decode('utf-8')
        new_item = Item.objects.first()

        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(new_item.text, 'A new list item')


    def test_redirects_after_POST(self):
        response = self.client.post("/", data={'item_text': 'A new task item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/")