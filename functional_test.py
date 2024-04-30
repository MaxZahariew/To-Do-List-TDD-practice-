from selenium import webdriver

import unittest


class NewVisitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_todo_list(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('To Do', self.browser.title,
                      msg='Увы это неверный заголовок')
        self.fail('Finish test')


if __name__ == '__main__':
    unittest.main()
