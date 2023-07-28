

class SearchPage:

    def __init__(self,driver):
        self.driver=driver

    valid_product_linktext="HP LP3065"

    def display_status_of_product(self):
        self.driver.find_element_by_linktext(self.valid_product_linktext).displayed
