from base.base_test import BaseTest
import time


class TestFirst(BaseTest):

    def test_login(self):
        self.login_page.open()
        time.sleep(10)