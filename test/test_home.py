from base.base_test import BaseTest
import pytest
import time


link = "https://google.com"

class TestMainPage1(BaseTest):

    def test_guest_should_see_login_link(self, driver):
        driver.get(link)