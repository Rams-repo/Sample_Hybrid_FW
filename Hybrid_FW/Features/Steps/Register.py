from behave import *

from Hybrid_FW.Utilities import MailIDGenerator


@given(u'I navigate to Register Page')
def step_impl(context):
    context.home_page.select_my_account()
    context.home_page.select_register_button()


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    for rows in context.table:
        context.register_page.enter_first_name(rows["first_name"])
        context.register_page.enter_last_name(rows["last_name"])

        new_mail = MailIDGenerator.get_new_mailid()
        context.register_page.enter_mail_id(new_mail)

        context.register_page.enter_telephone(rows["telephone"])
        context.register_page.enter_password(rows["password"])
        context.register_page.enter_pwd_confirm(rows["password"])


@when(u'I select Privacy policy option')
def step_impl(context):
    context.register_page.click_agree_button()


@when(u'I click on continue button')
def step_impl(context):
    context.register_page.click_continue_btn()


@then(u'Account should get created')
def step_impl(context):
    context.account_success_page.verify_account_created("Your Account Has Been Created!")


@when(u'I enter below details into all fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])

        new_mail = MailIDGenerator.get_new_mailid()
        context.register_page.enter_mail_id(new_mail)

        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_pwd_confirm(row["password"])
        context.register_page.select_newsletter()


@when(u'I enter below details into all fields except mail field')
def step_impl(context):
    for rows in context.table:
        context.register_page.enter_first_name(rows["first_name"])
        context.register_page.enter_last_name(rows["last_name"])
        context.register_page.enter_telephone(rows["telephone"])
        context.register_page.enter_password(rows["password"])
        context.register_page.enter_pwd_confirm(rows["password"])
        context.register_page.click_agree_button()


@when(u'I enter existing accounts email as "{email}" into email field')
def step_impl(context,email):
    context.register_page.enter_mail_id(email)


@then(u'Proper warning message should be displayed as "{warning_msg}"')
def step_impl(context,warning_msg):
    context.register_page.verify_existing_user_warning_msg(warning_msg)


@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_mail_id("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_pwd_confirm("")


@then(u'Proper warning message for all fields should be displayed')
def step_impl(context):
    context.register_page.display_all_warning_messages("First Name must be between 1 and 32 characters!",
                                                       "Last Name must be between 1 and 32 characters!",
                                                       "E-Mail Address does not appear to be valid!",
                                                       "Telephone must be between 3 and 32 characters!",
                                                       "Password must be between 4 and 20 characters!",
                                                       "Warning: You must agree to the Privacy Policy!")
    # context.register_page.verify_fname_warning_msg()
    # context.register_page.verify_lname_warning_msg()
    # context.register_page.verify_mail_warning_msg()
    # context.register_page.verify_telephone_warning_msg()
    # context.register_page.verify_password_warning_msg()
    # context.register_page.verify_policy_warning_msg()