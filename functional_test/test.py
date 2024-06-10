from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
from selenium import webdriver
import unittest

import time

MAX_WAITE = 5


class NewVisitTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def wait_for_row_in_list_tabel(self, row_text):
        start_time = time.time()
        try:
            table = self.browser.find_element(By.ID, "id_list_table")
            rows = table.find_elements(By.TAG_NAME, "tr")
            self.assertIn(row_text, [row.text for row in rows])
        except(AssertionError, WebDriverException) as err:
            if time.time() - start_time > MAX_WAITE:
                raise err
            time.sleep(0.5)

    # def test_can_start_todo_list(self):
    #     self.browser.get(self.live_server_url)

    #     self.assertIn("To Do", self.browser.title)

    #     # Предлагается ввести элемент списка
    #     inputbox = self.browser.find_element(By.ID, "id_new_item")
    #     self.assertCountEqual(
    #         inputbox.get_attribute('placeholder'),
    #         'Enter a to-do item'
    #     )

    #     # Записывае задачу
    #     inputbox.send_keys('Купить павлиньи перья')

    #     # Нажимаем на кнопку
    #     inputbox.send_keys(Keys.ENTER)
    #     time.sleep(1)

    #     self.wait_for_row_in_list_tabel('1: Купить павлиньи перья')

    #     self.browser.refresh()

    #     inputbox = self.browser.find_element(By.ID, "id_new_item")

    #     inputbox.send_keys('Сделать мушку из павлиньих перьев')

    #     inputbox.send_keys(Keys.ENTER)
    #     time.sleep(1)

    #     self.wait_for_row_in_list_tabel('1: Купить павлиньи перья')
    #     self.wait_for_row_in_list_tabel('2: Сделать мушку из павлиньих перьев')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys('Купить протеин')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_tabel("1: Купить протеин")

        maxim_list_url = self.browser.current_url
        self.assertRegex(maxim_list_url, "/lists/.+")

        self.browser.delete_all_cookies()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn('Купить протеин', page_text)
        self.assertNotIn('Сделать коктель', page_text)

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys('Купить бомбары')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_tabel("1: Купить бомбары")

        jenia_list_url = self.browser.current_url
        self.assertRegex(jenia_list_url, '/lists/.+')
        self.assertNotEqual(maxim_list_url, jenia_list_url)

        page_text = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertNotIn('Купить протени', page_text)
        self.assertIn("Куптиь бомбары", page_text)
