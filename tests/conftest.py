import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
