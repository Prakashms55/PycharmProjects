from page.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    valid_product_xpath="//a[normalize-space()='HP LP3065']"
    no_product_message_xpath="//p[text()='There is no product that matches the search criteria.']"

    def display_status_of_product(self):
        actual= self.display_search_product_detail("valid_product_xpath",self.valid_product_xpath)
        return actual
        # return self.driver.find_element_by_link_text(self.valid_product_link_text).is_displayed()

    def display_no_product_msg(self):
        expected="There is no product that matches the search criteria."
        actual=self.get_the_text("no_product_message_xpath",self.no_product_message_xpath)
        # actual=self.driver.find_element_by_xpath(self.no_product_message_xpath).text
        return actual.__eq__(expected)

