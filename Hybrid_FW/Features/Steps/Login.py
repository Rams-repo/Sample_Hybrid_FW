from behave import *
from Hybrid_FW.Utilities import MailIDGenerator


@given(u'I navigate to Login page')
def step_impl(context):
    context.home_page.select_my_account()
    context.home_page.select_login_button()


@when(u'I enter valid email id as "{email}" and password as "{password}"')
def step_impl(context,email,password):
    context.login_page.enter_username(email)
    context.login_page.enter_password(password)


@then(u'I click on login button')
def step_impl(context):
    context.login_page.click_login_button()


@then(u'I should login to home page as {title}')
def step_impl(context,title):
    context.account_page.verify_account_page(title)


@when(u'I enter invalid email id and valid password as "{password}"')
def step_impl(context,password):
    invalid_email = MailIDGenerator.get_new_mailid()
    context.login_page.enter_username(invalid_email)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message as "{warning_msg}"')
def step_impl(context,warning_msg):
    context.login_page.display_status_warning(warning_msg)


@when(u'I enter valid email id as "{mailid}" and invalid password as "{password}"')
def step_impl(context,mailid,password):
    context.login_page.enter_username(mailid)
    context.login_page.enter_password(password)


@when(u'I enter invalid email id and invalid password as "{password}"')
def step_impl(context,password):
    invalid_email = MailIDGenerator.get_new_mailid()
    context.login_page.enter_username(invalid_email)
    context.login_page.enter_password(password)


@when(u'I dont enter email id and password')
def step_impl(context):
    context.login_page.enter_username("")
    context.login_page.enter_password("")
