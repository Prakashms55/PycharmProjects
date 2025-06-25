from page.BasePage import BasePage
from page.RegisterPage import RegisterPage
from page.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    search_box_field_name="search"
    search_button_xpath="//button[@class='btn btn-default btn-lg']"
    click_my_account_xpath="//span[normalize-space()='My Account']"
    click_register_button_xpath="//a[normalize-space()='Register']"

    def enter_search_box_field(self,productname):
        self.type_into_element("search_box_field_name",self.search_box_field_name,productname)
        # self.driver.find_element_by_name(self.search_box_field_name).click()
        # self.driver.find_element_by_name(self.search_box_field_name).clear()
        # self.driver.find_element_by_name(self.search_box_field_name).send_keys(productname)

    def click_search_button(self):
        self.click_on_element("search_button_xpath",self.search_button_xpath)
        # self.driver.find_element_by_xpath(self.search_button_xpath).click()
        return SearchPage(self.driver)
    def search_for_a_product(self,productname):
        self.enter_search_box_field(productname)
        return self.click_search_button()
    def click_account_button(self):
        self.click_on_element("click_my_account_xpath",self.click_my_account_xpath)
        # self.driver.find_element_by_xpath(self.click_my_account_xpath).click()

    def click_register_button(self):
        self.click_on_element("click_register_button_xpath",self.click_register_button_xpath)
        # self.driver.find_element_by_xpath(self.click_register_button_xpath).click()
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.click_account_button()
        return self.click_register_button()
