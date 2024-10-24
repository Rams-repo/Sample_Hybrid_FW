from selenium.webdriver.common.by import By

from Hybrid_FW.Features.Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    login_page_title_xpath = "//title[normalize-space()='Account Login']"
    username_xpath = "//input[@id='input-email']"
    password_xpath = "//input[@id='input-password']"
    login_btn_xpath = "//input[@value='Login']"
    warning_msg_xpath = "//div[@id='account-login']/div[1]"

    def verify_login_page_title(self,expected_text):
        self.retrieved_element_text_equals("login_page_title_xpath", self.login_page_title_xpath, expected_text)
        #assert self.driver.find_element(*self.login_page_title_xpath).text.__eq__("Account Login")

    def enter_username(self, user_name):
        self.type_into_element("username_xpath",self.username_xpath,user_name)
        #self.driver.find_element(*self.username_xpath).send_keys(user_name)

    def enter_password(self, password):
        self.type_into_element("password_xpath",self.password_xpath,password)
        #self.driver.find_element(*self.password_xpath).send_keys(password)

    def click_login_button(self):
        self.click_on_element("login_btn_xpath", self.login_btn_xpath)
        #self.driver.find_element(*self.login_btn_xpath).click()

    def display_status_warning(self,expected_text):
        self.retrieved_element_text_equals("warning_msg_xpath", self.warning_msg_xpath, expected_text)
        #self.driver.find_element(*self.warning_msg_xpath).text.__eq__("Warning: No match for E-Mail Address and/or Password.")
