from selenium.webdriver.common.by import By

from miniSeleniumProject.pageObjectModel.checkout_PgObjModel import Checkout


class HomePage:
    def __init__(self, driver):
        self.driver = driver  # Store the driver

    shop = (By.XPATH, "//*[text()='Shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    like = (By.ID, "exampleCheck1")
    emp_status = (By.CSS_SELECTOR, "input#inlineRadio1")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    status_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    data_binding = (By.XPATH, "(//input[@name='name'])[2]")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = Checkout(self.driver)
        return checkoutPage

    def empName(self):
        return self.driver.find_element(*HomePage.name)

    def empEmail(self):
        return self.driver.find_element(*HomePage.email)

    def empPassword(self):
        return self.driver.find_element(*HomePage.password)

    def empGender(self):
        return self.driver.find_element(*HomePage.gender)

    def empLike(self):
        return self.driver.find_element(*HomePage.like)

    def empStatus(self):
        return self.driver.find_element(*HomePage.emp_status)

    def empSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def empStatusMsg(self):
        return self.driver.find_element(*HomePage.status_msg)

    def empDataBinding(self):
        return self.driver.find_element(*HomePage.data_binding)
