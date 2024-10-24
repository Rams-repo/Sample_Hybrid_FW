from behave import *


@given(u'I navigate to home page')
def step_impl(context):
    context.home_page.verify_home_page_title("Qafox.com")


@when(u'I search for a valid product "{product}" in search box')
def step_impl(context,product):
    context.home_page.enter_product(product)


@then(u'I click on Search button')
def step_impl(context):
    context.home_page.click_search_button()


@then(u'Product information and details should be displayed')
def step_impl(context):
    context.search_page.verify_product_displayed()


@when(u'I search for an invalid product "{product}" in search box')
def step_impl(context,product):
    context.home_page.enter_product(product)


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    context.search_page.verify_product_not_found_msg("There is no product that matches the search criteria.")


@when(u'I don\'t enter anything into search box')
def step_impl(context):
    context.home_page.enter_product("")
