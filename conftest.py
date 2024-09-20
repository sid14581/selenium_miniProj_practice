import inspect
import logging
import time

import pytest
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from miniSeleniumProject.Utils.BaseClass import *


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


driver = None


@pytest.fixture(scope="class")
def driverSetup(request):
    global driver
    # browser = str(input("browser you want to run --> "))
    browser = request.config.getoption("browser_name")
    if browser.lower() == "chrome".lower():
        url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\chromedriver-win64\chromedriver.exe")
        driver = wd.Chrome(service=url)
    elif browser.lower() == "edge".lower():
        url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\edgedriver_win64\msedgedriver.exe")
        driver = wd.Edge(service=url)
    elif browser.lower() == "firefox".lower():
        driver = wd.Firefox()

    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.close()
