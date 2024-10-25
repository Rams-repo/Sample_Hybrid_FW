from selenium.webdriver.common.by import By

from Hybrid_FW.Features.Pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    product_info_link_text = "HP LP3065"
    product_error_msg_xpath = "//p[contains(text(),'There is no product that matches the search criter')]"

    def verify_product_displayed(self):
        assert self.display_status("product_info_link_text", self.product_info_link_text)

    def verify_product_not_found_msg(self, expected_product_warning):
        self.retrieved_element_text_equals("product_error_msg_xpath", self.product_error_msg_xpath,
                                           expected_product_warning)
