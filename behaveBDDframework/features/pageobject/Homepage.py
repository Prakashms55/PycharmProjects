from features.pageobject.BasePage import BasePage
from features.pageobject.RegisterPage import RegisterPage
from features.pageobject.searchPage import searchPage


class Homepage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    search_box_name="search"
    click_search_button_xpath="//button[@class='btn btn-default btn-lg']"
    click_myAccount_xpath = "//span[normalize-space()='My Account']"
    click_register_xpath = "//a[normalize-space()='Register']"

    def send_keys_searchBar(self,search):
        # self.driver.find_element_by_name(self.search_box_name).send_keys(search)
        self.type_into_element( 'search_box_name',self.search_box_name,search)
    def click_search(self):
        self.click_on_element("click_search_button_xpath",self.click_search_button_xpath)
        return searchPage(self.driver)

    def verify_homePage(self,expectedtitle):
        return  self.verify_HOMEPAGE(expectedtitle)

    def click_myAccount(self):
        self.click_on_element("click_myAccount_xpath",self.click_myAccount_xpath)
        return RegisterPage(self.driver)

    def click_register(self):
        self.click_on_element("click_register_xpath",self.click_register_xpath)