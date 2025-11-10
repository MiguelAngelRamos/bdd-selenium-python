from pytest_bdd import given, when, then, parsers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from pages.login_page import LoginPage

@given('el usuario está en la página de login')
def navigate_to_login(selenium, base_url):
    login_page = LoginPage(selenium, base_url)
    login_page.open()

@when(parsers.parse('ingresa usuario "{username}"'))
def enter_username(selenium, base_url, username):
    login_page = LoginPage(selenium, base_url)
    login_page.enter_username(username)

@when(parsers.parse('ingresa contraseña "{password}"'))
def enter_password(selenium, base_url,password):
    login_page = LoginPage(selenium, base_url)
    login_page.enter_password(password)

@when('hace clic en el botón de inicio sesión')
def click_login(selenium, base_url):
    login_page = LoginPage(selenium, base_url)
    login_page.click_login_button()

@then('debería ver la página principal')
def verify_successful_login(selenium, base_url):
    """ Verificar que el usuario vea la página principal despues del login"""

    # Espera hasta 10 segundos a que se cumpla la condicion de redireccion
    WebDriverWait(selenium, 10).until(
        lambda driver: driver.current_url.endswith("/index.html")
        or driver.current_url == f"{base_url}/"
        or driver.current_url == base_url
    )

    login_page = LoginPage(selenium, base_url)

    # Comprobar que el menu de usuario sea visible, si no lo es, lanzaremos un error 
    assert login_page.is_user_menu_visible(), "User menu not visible after login"

