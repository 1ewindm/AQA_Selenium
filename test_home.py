import selenium
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

def test_navigate():
    driver.get("https://google.com")