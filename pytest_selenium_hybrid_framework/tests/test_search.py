import pytest
from selenium import webdriver

from page.HomePage import HomePage
from page.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class Testsearch:
    def test_search_send_valid_product(self):
        home_page=HomePage()
        home_page.enter_search_box_field("hp")
        home_page.click_search_button()
        search_page=SearchPage()
        assert search_page.display_status_of_product()
        # self.driver.find_element_by_name("search").send_keys("hp")
        # self.driver.find_element_by_xpath("//button[@class='btn btn-default btn-lg']").click()
        # assert self.driver.find_element_by_link_text("HP LP3065").is_displayed()

    def test_without_entering_search(self):
        self.driver.find_element_by_name("search").send_keys("")
        self.driver.find_element_by_xpath("//button[@class='btn btn-default btn-lg']").click()
        actual=self.driver.find_element_by_xpath("//p[contains(text(),'There is no product that matches the search criter')]").text
        expected="There is no product that matches the search criteria."
        assert actual.__eq__(expected)

    def test_search_send_invalid_product(self):
        self.driver.find_element_by_name("search").send_keys("honda")
        self.driver.find_element_by_xpath("//button[@class='btn btn-default btn-lg']").click()
        actual = self.driver.find_element_by_xpath(
            "//p[contains(text(),'There is no product that matches the search criter')]").text
        expected = "There is no product that matches the search criteria."
        assert actual.__eq__(expected)