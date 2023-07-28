

class Loginpage:
    email_id=''
    password_id=''
    login_btn_xpath=''
    logout_btn_xpath=''

    def __init__(self,driver):
        self.driver=driver

    def enter_email(self, username):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.Password_id).clear()
        self.driver.find_element_by_id(self.Password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_btn_xpath).click()