import inspect
import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("driverSetup")
class BaseClass:

    def waiting_element(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, element)))

    def waiting_tuple_element(self, tuple_element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(tuple_element))

    def selectOption(self, locator, gender):
        sel = Select(locator)
        sel.select_by_visible_text(gender)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        print(loggerName)
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler(r"C:\Users\siddh\PycharmProjects\pythonProject\miniSeleniumProject\Logs"
                                          r"\logfile_"+str(loggerName)+".log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)

        return logger
