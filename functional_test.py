from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest

import time


class NewVisitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        rows = []
        table = self.browser.find_element(By.ID, 'id_list_table')
        s = table.find_element(By.TAG_NAME, 'tr')
        rows.append(s.text)
        self.assertIn(row_text, [row for row in rows])

    def test_can_start_todo_list(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("To Do", self.browser.title)

        # Предлагается ввести элемент списка
        inputbox = self.browser.find_element(By.NAME, 'item_text')
        self.assertCountEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Записывае задачу
        inputbox.send_keys('Купить павлиньи перья')

        # Нажимаем на кнопку
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        self.check_for_row_in_list_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element(By.NAME, 'item_text')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')


if __name__ == '__main__':
    unittest.main()
