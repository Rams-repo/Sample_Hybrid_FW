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
        #self.driver.find_element(*self.page_text_xpath).text.__eq__("Register Account")

    def enter_first_name(self, f_name):
        self.type_into_element("f_name_id", self.f_name_id, f_name)
        #self.driver.find_element(*self.f_name_id).send_keys(f_name)

    def enter_last_name(self, l_name):
        self.type_into_element("l_name_id", self.l_name_id, l_name)
        #self.driver.find_element(*self.l_name_id).send_keys(l_name)

    def enter_mail_id(self, mailid):
        self.type_into_element("email_id", self.email_id, mailid)
        #self.driver.find_element(*self.email_id).send_keys(mailid)

    def enter_telephone(self, phone_no):
        self.type_into_element("telephone_id", self.telephone_id, phone_no)
        #self.driver.find_element(*self.telephone_id).send_keys(phone_no)

    def enter_password(self, pwd):
        self.type_into_element("password_id", self.password_id, pwd)
        #self.driver.find_element(*self.password_id).send_keys(pwd)

    def enter_pwd_confirm(self, c_pwd):
        self.type_into_element("confirm_password_id", self.confirm_password_id, c_pwd)
        #self.driver.find_element(*self.confirm_password_id).send_keys(c_pwd)

    def select_newsletter(self):
        self.click_on_element("subscribe_xpath", self.subscribe_xpath)
        #self.driver.find_element(*self.subscribe_xpath).click()

    def click_agree_button(self):
        self.click_on_element("agree_button_xpath", self.agree_button_xpath)
        #self.driver.find_element(*self.agree_button_xpath).click()

    def click_continue_btn(self):
        self.click_on_element("continue_btn_xpath", self.continue_btn_xpath)
        #self.driver.find_element(*self.continue_btn_xpath).click()

    def verify_existing_user_warning_msg(self, expected_warning_user):
        self.retrieved_element_text_contains("existing_user_warning_msg_xpath", self.existing_user_warning_msg_xpath,
                                             expected_warning_user)
        # actual_text = self.driver.find_element(*self.existing_user_warning_msg_xpath).text.strip().lower()
        # assert actual_text == "warning: e-mail address is already registered!", \
        #     f"Expected 'Warning: E-Mail Address is already registered!' but got '{actual_text}"

        # assert self.driver.find_element(*self.existing_user_warning_msg).text.__contains__("Warning: E-Mail Address is already registered!")

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

    # def verify_lname_warning_msg(self,expected_warning_lname):
    #     self.retrieved_element_text_contains("last_name_warning_xpath", *self.last_name_warning_xpath, expected_warning_lname)
    #     # assert self.driver.find_element(*self.last_name_warning_xpath)\
    #     #     .text.__contains__("Last Name must be between 1 and 32 characters!")
    #
    # def verify_fname_warning_msg(self,expected_warning_fname):
    #     self.retrieved_element_text_contains("first_name_warning_xpath",*self.first_name_warning_xpath,expected_warning_fname)
    #     #assert self.driver.find_element(*self.first_name_warning_xpath)\
    #     # .text.__contains__("First Name must be between 1 and 32 characters!")
    #
    # def verify_mail_warning_msg(self,expected_warning_mail):
    #     self.retrieved_element_text_contains("email_warning_xpath", *self.email_warning_xpath, expected_warning_mail)
    #     # assert self.driver.find_element(*self.email_warning_xpath)\
    #     #     .text.__contains__("E-Mail Address does not appear to be valid!")
    #
    # def verify_telephone_warning_msg(self,expected_warning_tele):
    #     self.retrieved_element_text_contains("telephone_warning_xpath", *self.telephone_warning_xpath, expected_warning_tele)
    #     # assert self.driver.find_element(*self.telephone_warning_xpath)\
    #     #     .text.__contains__("Telephone must be between 3 and 32 characters!")
    #
    # def verify_password_warning_msg(self,expected_warning_pwd):
    #     self.retrieved_element_text_contains("password_warning_xpath", *self.password_warning_xpath, expected_warning_pwd)
    #     # assert self.driver.find_element(*self.password_warning_xpath)\
    #     #     .text.__contains__("Password must be between 4 and 20 characters!")
    #
    # def verify_policy_warning_msg(self,expected_warning_policy):
    #     self.retrieved_element_text_contains("policy_warning_xpath", *self.policy_warning_xpath, expected_warning_policy)
    #     # assert self.driver.find_element(*self.policy_warning_xpath)\
    #     #     .text.__contains__("Warning: You must agree to the Privacy Policy!")
    #
