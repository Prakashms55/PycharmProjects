from page.HomePage import HomePage
from tests.BaseTest import BaseTest


class Testregister(BaseTest):
    def test_register_with_mandatory_field(self):
        home_page=HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()
        # home_page.click_account_button()
        # register_page=home_page.click_register_button()
        register_page.create_account("arjun", "r", "arjuns5565ss@gmail.com", "789896543", "arjun@55", "arjun@55","select")
        # register_page.enter_first_name("arjun")
        # register_page.enter_last_name("r")
        # register_page.enter_email("arjun12345ss@gmail.com")
        # register_page.enter_telephone("789896543")
        # register_page.enter_password("arjun@55")
        # register_page.re_enter_password("arjun@55")
        # register_page.click_agree_button()
        # register_page.click_continue_button()
        assert register_page.verify_account_created_msg()

        # self.driver.find_element_by_xpath("//span[normalize-space()='My Account']").click()
        # self.driver.find_element_by_xpath("//a[normalize-space()='Register']").click()
        # self.driver.find_element_by_id("input-firstname").send_keys("praveen")
        # self.driver.find_element_by_id("input-lastname").send_keys("p")
        # self.driver.find_element_by_id("input-email").send_keys("praveenpp1235rQ@gmail.com")
        # self.driver.find_element_by_id("input-telephone").send_keys("8796543213")
        # self.driver.find_element_by_id("input-password").send_keys("praveen55")
        # self.driver.find_element_by_id("input-confirm").send_keys("praveen55")
        # self.driver.find_element_by_name("agree").click()
        # self.driver.find_element_by_xpath("//input[@value='Continue']").click()
        # actual=self.driver.find_element_by_xpath("//div[@id='content']//h1").text
        # expected="Your Account Has Been Created!"
        # assert actual.__eq__(expected)

    def test_register_with_existing_account(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()
        # home_page.click_account_button()
        # register_page=home_page.click_register_button()
        register_page.create_account("arjun","r","arjun125ss@gmail.com","789896543","arjun@55","arjun@55","select")
        # register_page.enter_first_name("arjun")
        # register_page.enter_last_name("r")
        # register_page.enter_email("arjun12ss@gmail.com")
        # register_page.enter_telephone("789896543")
        # register_page.enter_password("arjun@55")
        # register_page.re_enter_password("arjun@55")
        # register_page.click_agree_button()
        # register_page.click_continue_button()
        assert register_page.warning_already_account_created_msg()

        # self.driver.find_element_by_xpath("//span[normalize-space()='My Account']").click()
        # self.driver.find_element_by_xpath("//a[normalize-space()='Register']").click()
        # self.driver.find_element_by_id("input-firstname").send_keys("praveen")
        # self.driver.find_element_by_id("input-lastname").send_keys("p")
        # self.driver.find_element_by_id("input-email").send_keys("praveenp123Q@gmail.com")
        # self.driver.find_element_by_id("input-telephone").send_keys("8796543213")
        # self.driver.find_element_by_id("input-password").send_keys("praveen55")
        # self.driver.find_element_by_id("input-confirm").send_keys("praveen55")
        # self.driver.find_element_by_name("agree").click()
        # self.driver.find_element_by_xpath("//input[@value='Continue']").click()
        # actual=self.driver.find_element_by_xpath("//div[@class='alert alert-danger alert-dismissible']").text
        # expected="Warning: E-Mail Address is already registered!"
        # assert actual.__contains__(expected)