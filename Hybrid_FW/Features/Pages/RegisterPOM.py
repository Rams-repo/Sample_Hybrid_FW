from Hybrid_FW.Features.Pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    page_text_xpath = "//h1[normalize-space()='Register Account']"
    f_name_id = "input-firstname"
    l_name_id = "input-lastname"
    email_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    confirm_password_id = "input-confirm"

    subscribe_xpath = "//label[normalize-space()='Yes']"
    agree_button_xpath = "//input[@name='agree']"

    continue_btn_xpath = "//input[@value='Continue']"

    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"
    policy_warning_xpath = "//div[@id='account-register']/div[1]"

    existing_user_warning_msg_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def register_page_verify(self, expected_text):
        self.retrieved_element_text_equals("page_text_xpath", self.page_text_xpath, expected_text)

    def enter_first_name(self, f_name):
        self.type_into_element("f_name_id", self.f_name_id, f_name)

    def enter_last_name(self, l_name):
        self.type_into_element("l_name_id", self.l_name_id, l_name)

    def enter_mail_id(self, mailid):
        self.type_into_element("email_id", self.email_id, mailid)

    def enter_telephone(self, phone_no):
        self.type_into_element("telephone_id", self.telephone_id, phone_no)

    def enter_password(self, pwd):
        self.type_into_element("password_id", self.password_id, pwd)

    def enter_pwd_confirm(self, c_pwd):
        self.type_into_element("confirm_password_id", self.confirm_password_id, c_pwd)

    def select_newsletter(self):
        self.click_on_element("subscribe_xpath", self.subscribe_xpath)

    def click_agree_button(self):
        self.click_on_element("agree_button_xpath", self.agree_button_xpath)

    def click_continue_btn(self):
        self.click_on_element("continue_btn_xpath", self.continue_btn_xpath)

    def verify_existing_user_warning_msg(self, expected_warning_user):
        self.retrieved_element_text_contains("existing_user_warning_msg_xpath", self.existing_user_warning_msg_xpath,
                                             expected_warning_user)

    def display_all_warning_messages(self, expected_warning_fname, expected_warning_lname, expected_warning_mail,
                                     expected_warning_tele, expected_warning_pwd, expected_warning_policy):
        self.retrieved_element_text_contains("first_name_warning_xpath", self.first_name_warning_xpath,
                                             expected_warning_fname)
        self.retrieved_element_text_contains("last_name_warning_xpath", self.last_name_warning_xpath,
                                             expected_warning_lname)
        self.retrieved_element_text_contains("email_warning_xpath", self.email_warning_xpath, expected_warning_mail)
        self.retrieved_element_text_contains("telephone_warning_xpath", self.telephone_warning_xpath,
                                             expected_warning_tele)
        self.retrieved_element_text_contains("password_warning_xpath", self.password_warning_xpath,
                                             expected_warning_pwd)
        self.retrieved_element_text_contains("policy_warning_xpath", self.policy_warning_xpath,
                                             expected_warning_policy)
