from selenium.webdriver.common.by import By

from Hybrid_FW.Features.Pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_confirmation_xpath = "//div[@id='content']/h2"

    def verify_account_page(self, expected_text):
        return self.retrieved_element_text_contains("account_confirmation_xpath",
                                                    self.account_confirmation_xpath, expected_text)
