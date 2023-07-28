import time

from selenium import webdriver
import pytest
from pageobject.loginpage import loginpage
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen


class Test_001_login:
    base_url=Readconfig.getapplicationurl()
    email=Readconfig.getuseremail()
    password=Readconfig.getpassword()
    logger=LogGen.loggen()

    def test_homepage_title(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver=setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.base_url)
        tile=self.driver.title

        if tile=="Your store. Login":
            self.driver.get_screenshot_as_file(filename='C://Users//praka//PycharmProjects//hybrid_framework//screenshots//test_homepage_title.png')
            # self.driver.close()
            assert True
        else:
            assert False
            # self.driver.close()
        self.driver.close()
    def test_login_01(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp=loginpage(self.driver)
        self.lp.enter_email(self.email)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        act_title=self.driver.title
        self.logger.info("verify that browser launched in right page")
        if act_title=="Dashboard / nopCommerce administration":
            self.driver.get_screenshot_as_file(filename="C://Users//praka//PycharmProjects//hybrid_framework//screenshots//test01.png")
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
