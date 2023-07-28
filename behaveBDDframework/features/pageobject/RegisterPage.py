from features.pageobject.BasePage import BasePage
class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    verify_registerPage_xpath="//h1[normalize-space()='Register Account']"
    enter_fname_id="input-firstname"
    enter_lname_id="input-lastname"
    enter_email_id="input-email"
    enter_telephone_id="input-telephone"
    enter_password_id="input-password"
    enter_reEnter_password_id="input-confirm"
    click_privacyPolicy_checkbox_xpath="//input[@name='agree']"
    click_continue_button_xpath="//input[@value='Continue']"
    verify_account_created_page_xpath="//div[@id='content']//h1"

    def verify_registerPage(self,expected):
        actual=self.driver.find_element_by_xpath(self.verify_registerPage_xpath).text
        return actual.__eq__(expected)

    def enter_fname(self,first_name):
        # self.driver.find_element_by_id(self.enter_fname_ID).send_keys(firstname)
        self.type_into_element('enter_fname_id', self.enter_fname_id ,first_name)

    def last_name(self,last_name):
        # self.driver.find_element_by_id(self.enter_lname_ID).send_keys(lastname)
        self.type_into_element('enter_lname_id',self.enter_lname_id,last_name)
    def email(self,email):
        # self.driver.find_element_by_id(self.enter_email_ID).send_keys(emailid)
        self.type_into_element('enter_email_id',self.enter_email_id,email)
    def enter_telephone(self,telephone):
        # self.driver.find_element_by_id(self.enter_telephone_ID).send_keys(tele)
        self.type_into_element('enter_telephone_id',self.enter_telephone_id,telephone)
    def enter_password(self,password):
        # self.driver.find_element_by_id(self.enter_password_ID).send_keys(pwd)
        self.type_into_element('enter_password_id',self.enter_password_id,password)
    def re_enter_pwd(self,reenterpwd):
        # self.driver.find_element_by_id(self.enter_reEnter_password_ID).send_keys(repwd)
        self.type_into_element('enter_reEnter_password_id',self.enter_reEnter_password_id,reenterpwd)
    def click_privacy(self):
        # self.driver.find_element_by_xpath(self.click_privacyPolicy_checkbox_xpath).click()
        self.click_on_element('click_privacyPolicy_checkbox_xpath',self.click_privacyPolicy_checkbox_xpath)
    def click_continue(self):
        # self.driver.find_element_by_xpath(self.click_continue_button_xpath).click()
        self.click_on_element('click_continue_button_xpath',self.click_continue_button_xpath)
    def  verify_account_created_page(self):
        expected="Your Account Has Been Created!"
        # actual_page=self.driver.find_element_by_xpath(self.verify_account_created_page_xpath).text
        # actual_page.__eq__(expected)
        self.verify_contains_page('verify_account_created_page_xpath',self.verify_account_created_page_xpath,expected)
        return True


