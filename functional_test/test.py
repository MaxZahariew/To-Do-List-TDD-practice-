from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium import webdriver
import unittest

import time


class NewVisitTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_todo_list(self):
        self.browser.get(self.live_server_url)

        self.assertIn("To Do", self.browser.title)

        # Предлагается ввести элемент списка
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertCountEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Записывае задачу
        inputbox.send_keys('Купить павлиньи перья')

        # Нажимаем на кнопку
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Купить павлиньи перья')

        self.browser.refresh()

        inputbox = self.browser.find_element(By.ID, "id_new_item")

        inputbox.send_keys('Сделать мушку из павлиньих перьев')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')
