import pytest

from DemoData.DemoData import HomePageData
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, setup, dataLoad):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Entering Name Test as Zahed")
        homepage.getName().send_keys(dataLoad["name"])
        log.info("Entering EMail Test")
        homepage.getEmail().send_keys(dataLoad["email"])
        log.info("Entering Password Test")
        homepage.getPass().send_keys(dataLoad["password"])
        log.info("Clicking on the checkbox")
        homepage.getCheck().click()
        log.info("Clicking on the Dropdown")
        self.getDropDown(homepage.getGender(), dataLoad["gender"])
        log.info("Clicking on the Radio Button")
        homepage.getRadio().click()
        log.info("Submitting the form")
        homepage.getSubmit().click()
        log.info("Getting the Message Text")
        msg = homepage.getText().text

        assert "Success!" in msg
        self.driver.refresh()

    # Data Driven System
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def dataLoad(self, request):
        return request.param
