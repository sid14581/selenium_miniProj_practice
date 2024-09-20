import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from miniSeleniumProject.TestData.HomePageData import HomePageData
from miniSeleniumProject.conftest import *
from miniSeleniumProject.pageObjectModel.home_PgObjModel import HomePage


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        log = self.getLogger()

        homepage.empName().send_keys(getData["name"])
        homepage.empEmail().send_keys(getData["email"])
        homepage.empPassword().send_keys(getData["password"])
        homepage.empLike().click()
        log.info("firstname "+getData["name"])

        self.selectOption(homepage.empGender(), getData["gender1"])
        time.sleep(3)
        self.selectOption(homepage.empGender(), getData["gender2"])

        homepage.empStatus().click()
        homepage.empSubmit().click()

        emp_msg = homepage.empStatusMsg().text
        print(emp_msg.replace("×", "").strip())

        assert "Success" in emp_msg

        homepage.empDataBinding()
        time.sleep(2)
        homepage.empDataBinding().clear()

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_testData("Testcases_1"))
    def getData(self, request):
        return request.param
