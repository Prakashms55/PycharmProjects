

class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def getelement(self,locator_type, locator_value):
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

    def type_into_element(self,locator_type,locator_value,text):
        element=self.getelement(locator_type,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_on_element(self,locator_type,locator_value):
        element = self.getelement(locator_type,locator_value)
        element.click()

    def display_search_product_detail(self,locator_type,locator_value):
        element=self.getelement(locator_type,locator_value)
        return element.is_displayed()

    def get_the_text(self,locator_type,locator_value):
        element=self.getelement(locator_type,locator_value)
        element.text