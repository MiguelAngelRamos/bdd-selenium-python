
from pytest_bdd import scenarios, given, then,when, parsers;
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from pages.index_page import IndexPage
scenarios('../features/navigation.feature')
# parsers.parse('ingresa usuario "{username}"')

@given(parsers.re(r'el usuario ha iniciado sesión con usuario "(?P<username>\w+)" y contraseña "(?P<password>\w+)"'))
#@given(parsers.parse('el usuario ha iniciado sesión con usuario {username} y contraseña {password}'))
def user_logged_in(selenium, base_url, username, password):
    login_page = LoginPage(selenium, base_url)
    login_page.login(username, password)

    # Espera Explicita: Esperar hasta 10 segundos a que la URL contenga "index"
    # Esto confirma que el login fue exitoso y redirigio correctamente
    WebDriverWait(selenium, 10).until(EC.url_contains("index"))



@then('debería ver el menú de navegación')
def ver_menu_navegacion(selenium, base_url):
    index_page = IndexPage(selenium, base_url)
    assert index_page.navbar.is_navbar_visible(), "El menú de navegación no está visible"

@then(parsers.parse('debería ver el enlace "{link_text}"'))
def ver_enlace(selenium, base_url, link_text):
    index_page = IndexPage(selenium, base_url)

    if link_text == "Productos":
        assert index_page.navbar.is_products_link_visible(), "El enlace 'Productos' no está visible"
    elif link_text == "Carrito":
        assert index_page.navbar.is_cart_link_visible(), "El enlace 'Carrito' no está visible"
    else:
        raise ValueError(f"Step 'ver enlace' no definido para: {link_text}")


@when(parsers.parse('el usuario hace clic en el enlace "{link_text}"'))
def click_en_enlace(selenium, base_url, link_text):
    index_page = IndexPage(selenium, base_url)

    if link_text == "Productos":
        #!ERROR es por que aqui tenia assert eso paso por copiar y pegar el codigo no me fije que habia dejado los assert anteriores
        index_page.navbar.click_products()
    elif link_text == "Carrito":
        index_page.navbar.click_cart()
    else:
        raise ValueError(f"Step 'clic en enlace' no definido para: {link_text}")





@when("el usuario hace clic en cerrar sesión")
def click_cerrar_sesion(selenium, base_url):
    # Hace click en logout a través del componente
    index_page = IndexPage(selenium, base_url)
    index_page.navbar.click_logout()


