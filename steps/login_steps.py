from pytest_bdd import given, when, then, parsers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from pages.login_page import LoginPage

@given('el usuario está en la página de login')
def navigate_to_login(selenium):
    login_page = LoginPage(selenium)
    pass

@when(parsers.parse('ingresa usuario "{username}"'))
def enter_username(selenium, username):
    pass

@when(parsers.parse('ingresa contraseña "{password}"'))
def enter_password(selenium, password):
    pass

@when('hace clic en el botón de inicio sesión')
def click_login(selenium):
    pass

@then('debería ver la página principal')
def verify_successful_login(selenium):
    pass

