import pytest

from pages.login_page import LoginPage

class BaseTest:

    login_page: LoginPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)


