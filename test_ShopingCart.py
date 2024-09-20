import pytest
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from miniSeleniumProject.conftest import *
from miniSeleniumProject.pageObjectModel.checkout_PgObjModel import Checkout
from miniSeleniumProject.pageObjectModel.confirm_PgObjModel import Confirm
from miniSeleniumProject.pageObjectModel.home_PgObjModel import HomePage


class TestShoppingCart(BaseClass):

    def test_shoppingCart(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("getting all the card titles")
        # def test_checkoutPage(self):
        phones = ["iphone X", "Samsung Note 8", "Blackberry"]

        # checkoutPage = Checkout(self.driver)
        for phone in phones:
            yo1 = "//*[text()='" + str(phone) + "']"
            yo2 = yo1 + "/ancestor::div[@class='card h-100']//button"
            log.info(phone)
            self.waiting_element(yo2)
            self.driver.find_element(By.XPATH, yo2).click()

        self.waiting_tuple_element(checkoutPage.checkout)
        checkoutPage.checkOut()
        log.info("clicking checkout")
        self.waiting_tuple_element(checkoutPage.checkout)
        confirmPage = checkoutPage.checkOut()
        log.info("going to confirm page")
        # def test_confirmPage(self):
        country = "india".capitalize()
        confirmPage.conFirm().send_keys(country)
        ele = "//*[text()='" + country + "']"

        self.waiting_element(ele)
        self.driver.find_element(By.XPATH, ele).click()

        confirmPage.purChase().click()
        log.info("confirm page")
        self.waiting_tuple_element(confirmPage.status)
        status_msg = confirmPage.statusPage().text

        print(status_msg.replace("×", "").strip())

        assert "Success" in status_msg


