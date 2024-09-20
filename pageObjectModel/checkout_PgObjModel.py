from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from miniSeleniumProject.pageObjectModel.confirm_PgObjModel import Confirm


class Checkout:
    def __init__(self, driver):
        self.driver = driver  # Store the driver

    checkout = (By.XPATH, "//*[contains(text(),'Checkout')]")

    def checkOut(self):
        self.driver.find_element(*Checkout.checkout).click()
        confPage = Confirm(self.driver)
        return confPage
