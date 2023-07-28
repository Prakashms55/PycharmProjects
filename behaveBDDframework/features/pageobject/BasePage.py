
class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element_by_id(locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element_by_name(locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element_by_class_name(locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element_by_xpath(locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element_by_link_text(locator_value)
        return element

    def click_on_element(self,locator_type,locator_value):
        element=self.get_element(locator_type,locator_value)
        element.click()
    def type_into_element(self,locator_type,locator_value,text_to_be_entered):
        element=self.get_element(locator_type,locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_be_entered)

    def verify_HOMEPAGE(self,expectedtitle):
        return self.driver.title.__contains__(expectedtitle)

    def retrieve_element_text_and_verify(self,locator_type,locator_value):
        # element=self.driver.find_element_by_xpath(self.check_product_page_xpath).is_displayed()
        element=self.get_element(locator_type,locator_value)
        return element.is_displayed()

    def verify_contains_page(self,locator_type,locator_value,expected):
        element=self.get_element(locator_type,locator_value)
        return element.text.__contains__(expected)