

class HomePage:

    def __init__(self,driver):
        self.driver=driver

    search_box_field_name="search"
    search_button_xpath="//button[@class='btn btn-default btn-lg']"

    def enter_search_box_field(self,productname):
        self.driver.find_element_by_name(self.search_box_field_name).click()
        self.driver.find_element_by_name(self.search_box_field_name).clear()
        self.driver.find_element_by_name(self.search_box_field_name).send_keys(productname)

    def click_search_button(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
