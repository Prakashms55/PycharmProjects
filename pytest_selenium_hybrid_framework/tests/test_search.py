import allure
from allure_commons.types import AttachmentType

from page.HomePage import HomePage
from tests.BaseTest import BaseTest


class Testsearch(BaseTest):
    def test_search_send_valid_product(self):
        home_page=HomePage(self.driver)
        search_page=home_page.search_for_a_product("HP")
        # home_page.enter_search_box_field("hp")
        # search_page=home_page.click_search_button()
        assert search_page.display_status_of_product()
        # self.driver.find_element_by_name("search").send_keys("hp")
        # self.driver.find_element_by_xpath("//button[@class='btn btn-default btn-lg']").click()
        # assert self.driver.find_element_by_link_text("HP LP3065").is_displayed()

    def test_without_entering_search(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product(" ")
        # home_page.enter_search_box_field(" ")
        # search_page=home_page.click_search_button()
        assert search_page.display_no_product_msg()
        # self.driver.find_element_by_name("search").send_keys("")
        # self.driver.find_element_by_xpath("//button[@class='btn btn-default btn-lg']").click()
        # actual=self.driver.find_element_by_xpath("//p[contains(text(),'There is no product that matches the search criter')]").text
        # expected="There is no product that matches the search criteria."
        # assert actual.__eq__(expected)

    def test_search_send_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("honda")
        # home_page.enter_search_box_field(" ")
        # search_page=home_page.click_search_button()
        assert search_page.display_no_product_msg()
        # self.driver.find_element_by_name("search").send_keys("honda")
        # self.driver.find_element_by_xpath("//button[@class='btn btn-default btn-lg']").click()
        # actual = self.driver.find_element_by_xpath(
        #     "//p[contains(text(),'There is no product that matches the search criter')]").text
        # expected = "There is no product that matches the search criteria."
        # assert actual.__eq__(expected)