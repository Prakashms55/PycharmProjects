from page.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    first_name_id="input-firstname"
    last_name_id="input-lastname"
    email_id="input-email"
    telephone_id="input-telephone"
    password_id="input-password"
    re_enter_password_id="input-confirm"
    click_agree_button_name="agree"
    click_continue_button_xpath="//input[@value='Continue']"
    account_created_msg_xpath="//div[@id='content']//h1"
    warning_msg_xpath="//div[@class='alert alert-danger alert-dismissible']"
    def enter_first_name(self,fname):
        self.type_into_element("first_name_id",self.first_name_id,fname)
        # self.driver.find_element_by_id(self.first_name_id).click()
        # self.driver.find_element_by_id(self.first_name_id).clear()
        # self.driver.find_element_by_id(self.first_name_id).send_keys(fname)
    def enter_last_name(self,lname):
        self.type_into_element( "last_name_id",self.last_name_id, lname)
        # self.driver.find_element_by_id(self.last_name_id).click()
        # self.driver.find_element_by_id(self.last_name_id).clear()
        # self.driver.find_element_by_id(self.last_name_id).send_keys(lname)
    def enter_email(self,email):
        self.type_into_element( "email_id",self.email_id, email)
        # self.driver.find_element_by_id(self.email_id).click()
        # self.driver.find_element_by_id(self.email_id).clear()
        # self.driver.find_element_by_id(self.email_id).send_keys(email)
    def enter_telephone(self,tphone):
        self.type_into_element( "telephone_id",self.telephone_id, tphone)
        # self.driver.find_element_by_id(self.telephone_id).click()
        # self.driver.find_element_by_id(self.telephone_id).clear()
        # self.driver.find_element_by_id(self.telephone_id).send_keys(tphone)
    def enter_password(self,password):
        self.type_into_element("password_id",self.password_id, password)
        # self.driver.find_element_by_id(self.password_id).click()
        # self.driver.find_element_by_id(self.password_id).clear()
        # self.driver.find_element_by_id(self.password_id).send_keys(password)
    def re_enter_password(self,repwd):
        self.type_into_element( "re_enter_password_id",self.re_enter_password_id, repwd)
        # self.driver.find_element_by_id(self.re_enter_password_id).click()
        # self.driver.find_element_by_id(self.re_enter_password_id).clear()
        # self.driver.find_element_by_id(self.re_enter_password_id).send_keys(repwd)
    def click_agree_button(self):
        self.click_on_element("click_agree_button_name",self.click_agree_button_name)
        # self.driver.find_element_by_name(self.click_agree_button_name).click()
    def click_continue_button(self):
        self.click_on_element("click_continue_button_xpath",self.click_continue_button_xpath)
        # self.driver.find_element_by_xpath(self.click_continue_button_xpath).click()

    def verify_account_created_msg(self):
        expected = "Your Account Has Been Created!"
        actual=self.get_the_text("account_created_msg_xpath",self.account_created_msg_xpath)
        # actual = self.driver.find_element_by_xpath(self.account_created_msg_xpath).text
        return actual.__eq__(expected)

    def warning_already_account_created_msg(self):
        expected = "Warning: E-Mail Address is already registered!"
        actual=self.get_the_text("warning_msg_xpath",self.warning_msg_xpath)
        # actual = self.driver.find_element_by_xpath(self.warning_msg_xpath).text
        return actual.__eq__(expected)
    def create_account(self,fname,lname,email,mobile,pwd,repwd,select_not_select):
        self.enter_first_name(fname)
        self.enter_last_name(lname)
        self.enter_email(email)
        self.enter_telephone(mobile)
        self.enter_password(pwd)
        self.re_enter_password(repwd)
        if select_not_select.__eq__("select"):
            self.click_agree_button()
        self.click_continue_button()

