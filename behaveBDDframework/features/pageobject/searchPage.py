from features.pageobject.BasePage import BasePage


class searchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    check_product_page_xpath = "//div[@class='caption']//a"
    verify_message_xpath = "//div[@id='content']//p[2]"
    # check_product_page_link_text ='HP LP3065'

    def verify_page(self):
        return self.retrieve_element_text_and_verify('check_product_page_xpath',self.check_product_page_xpath)
    def verify_proper_message(self):
        expected = 'There is no product that matches the search criteria.'
        verify_message=self.driver.find_element_by_xpath(self.verify_message_xpath).text.__contains__(expected)
        if verify_message and expected:
            return True
        else:
            return False