from selenium.webdriver.common.by import By

from Hybrid_FW.Features.Pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    successful_msg_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def verify_account_created(self, expected_text):
        self.retrieved_element_text_equals("successful_msg_xpath", self.successful_msg_xpath, expected_text)
        #assert self.driver.find_element(*self.successful_msg_xpath).text.__eq__("Your Account Has Been Created!")
