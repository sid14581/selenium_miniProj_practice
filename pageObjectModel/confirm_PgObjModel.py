from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Confirm:
    def __init__(self, driver):
        self.driver = driver  # Store the driver

    confirm = (By.CSS_SELECTOR, "input[id='country']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    status = (By.XPATH, "//strong/parent::*")

    def conFirm(self):
        return self.driver.find_element(*Confirm.confirm)

    def purChase(self):
        return self.driver.find_element(*Confirm.purchase)

    def statusPage(self):
        return self.driver.find_element(*Confirm.status)
