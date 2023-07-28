import pytest
from selenium import webdriver

@pytest.mark.usefixtures("setup_and_teardown")
class Testregister:
    def test_register_with_mandatory_field(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='My Account']").click()
        self.driver.find_element_by_xpath("//a[normalize-space()='Register']").click()
        self.driver.find_element_by_id("input-firstname").send_keys("praveen")
        self.driver.find_element_by_id("input-lastname").send_keys("p")
        self.driver.find_element_by_id("input-email").send_keys("praveenpp1235rQ@gmail.com")
        self.driver.find_element_by_id("input-telephone").send_keys("8796543213")
        self.driver.find_element_by_id("input-password").send_keys("praveen55")
        self.driver.find_element_by_id("input-confirm").send_keys("praveen55")
        self.driver.find_element_by_name("agree").click()
        self.driver.find_element_by_xpath("//input[@value='Continue']").click()
        actual=self.driver.find_element_by_xpath("//div[@id='content']//h1").text
        expected="Your Account Has Been Created!"
        assert actual.__eq__(expected)

    def test_register_with_existing_account(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='My Account']").click()
        self.driver.find_element_by_xpath("//a[normalize-space()='Register']").click()
        self.driver.find_element_by_id("input-firstname").send_keys("praveen")
        self.driver.find_element_by_id("input-lastname").send_keys("p")
        self.driver.find_element_by_id("input-email").send_keys("praveenp123Q@gmail.com")
        self.driver.find_element_by_id("input-telephone").send_keys("8796543213")
        self.driver.find_element_by_id("input-password").send_keys("praveen55")
        self.driver.find_element_by_id("input-confirm").send_keys("praveen55")
        self.driver.find_element_by_name("agree").click()
        self.driver.find_element_by_xpath("//input[@value='Continue']").click()
        actual=self.driver.find_element_by_xpath("//div[@class='alert alert-danger alert-dismissible']").text
        expected="Warning: E-Mail Address is already registered!"
        assert actual.__contains__(expected)