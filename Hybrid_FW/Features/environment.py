from selenium import webdriver

from Hybrid_FW.Features.Pages.AccountPOM import AccountPage
from Hybrid_FW.Features.Pages.AccountSuccessPOM import AccountSuccessPage
from Hybrid_FW.Features.Pages.HomePOM import HomePage
from Hybrid_FW.Features.Pages.LoginPOM import LoginPage
from Hybrid_FW.Features.Pages.RegisterPOM import RegisterPage
from Hybrid_FW.Features.Pages.SearchPOM import SearchPage
from Hybrid_FW.Utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

    # Declared all the below pages in this hook to make the page objects available for all scenarios\
    # to prevent Atrribute error from occurring

    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.account_page = AccountPage(context.driver)
    context.register_page = RegisterPage(context.driver)
    context.account_success_page = AccountSuccessPage(context.driver)
    context.search_page = SearchPage(context.driver)


def after_scenario(context, driver):
    context.driver.quit()
