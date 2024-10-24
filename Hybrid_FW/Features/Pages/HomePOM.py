import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Hybrid_FW.Features.Pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    home_page_title_xpath = "//a[normalize-space()='Qafox.com']"
    my_account_xpath = "//span[normalize-space()='My Account']"
    login_button_xpath = "//a[normalize-space()='Login']"
    register_button_xpath = "//a[normalize-space()='Register']"

    searchbox_xpath = "//input[@placeholder='Search']"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"

    def verify_home_page_title(self,expected_title):
        time.sleep(2)
        # actual_text = self.driver.find_element(*self.home_page_title).text.strip().lower()
        # assert actual_text == "qafox.com", f"Expected 'Qafox.com' but got '{actual_text}'"
        return self.verify_page_title(expected_title)
        #assert self.driver.find_element(*self.home_page_title_xpath).text.__eq__("Qafox.com")

    def select_my_account(self):
        self.click_on_element("my_account_xpath", self.my_account_xpath)
        #self.driver.find_element(*self.my_account_xpath).click()

    def select_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        #self.driver.find_element(*self.login_button_xpath).click()

    def select_register_button(self):
        self.click_on_element("register_button_xpath", self.register_button_xpath)
        #self.driver.find_element(*self.register_button_xpath).click()

    def enter_product(self, product):
        self.type_into_element("searchbox_xpath", self.searchbox_xpath, product)
        #self.driver.find_element(*self.searchbox_xpath).send_keys(product)

    def click_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        #self.driver.find_element(*self.search_button_xpath).click()


