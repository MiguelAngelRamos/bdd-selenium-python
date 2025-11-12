
from pytest_bdd import scenarios, given, then,when, parsers;
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
scenarios('../features/navigation.feature')
# parsers.parse('ingresa usuario "{username}"')

#@given(parsers.re(r'el usuario ha iniciado sesión con usuario "(?P<username>\w+)" y contraseña "(?P<password>\w+)"'))
@given(parsers.parse('el usuario ha iniciado sesión con usuario {username} y contraseña {password}'))
def user_logged_in(selenium, base_url, username, password):
    login_page = LoginPage(selenium, base_url)
    login_page.login(username, password)

    # Espera Explicita: Esperar hasta 10 segundos a que la URL contenga "index"
    # Esto confirma que el login fue exitoso y redirigio correctamente
    WebDriverWait(selenium, 10).until(EC.url_contains("index"))

@given('el usuario está en la página principal')
def usuario_en_pagina_principal(selenium, base_url, context):
    selenium.get(f"{base_url}/index.html")

@then('debería ver el menú de navegación')
def ver_menu_navegacion(selenium):
    navbar = WebDriverWait(selenium, 10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "nav.navbar")))
    assert navbar.is_displayed()

@given(parsers.parse('debería ver el enlace "{link_text}"'))
def ver_enlace(selenium, link_text):
    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located(By.PARTIAL_LINK_TEXT, link_text))
    assert element.is_displayed()

@when(parsers.parse('el usuario hace clic en el enlace "{link_text}"'))
def click_en_enlace(selenium, link_text):
    """Un Soporte para menus responsive"""
    try:
        toggler = selenium.find_element(By.CLASS_NAME, "navbar-toggler")
        # Si el boton de hamburgesa es visible, en navbar esta calapsado y necesitamos expandirlo
        if toggler.is_displayed():
            toggler.click()
            # Esperar a que se el menu se expanda(espera explicita)
            WebDriverWait(selenium, 5).until(
                EC.visibility_of_element_located(By.PARTIAL_LINK_TEXT, link_text))
    except:
        pass

    element = WebDriverWait(selenium, 10).until(
        EC.visibility_of_element_located(By.PARTIAL_LINK_TEXT, link_text))
    
    selenium.execute_script("arguments[0].scrollIntoView(true);", element)
    WebDriverWait(selenium, 5).until(EC.visibility_of(element))
    selenium.execute_script("arguments[0].click();", element)


@then(parsers.pase('el usuario debería estar en la página "{page_name}"'))
def usuario_en_pagin(selenium, page_name):
    WebDriverWait(selenium, 15).until(
        lambda d: page_name in d.current_url,
        message=f"Esperaba estar en '{page_name} pero la URL ES: {selenium.current_url}"
    )
    assert page_name in selenium.current_url;

@when("el usuario hace clic en cerrar sesion")
def click_cerrar_sesion(selenium):
    # Primero hacer click en el menu de usuario
    user_menu = WebDriverWait(selenium, 10).until(
        EC.element_to_be_clickable(By.ID, "user-name")
    )
    selenium.execute_script("argument[0].scrollIntoView(true);", user_menu)
    # Esperar a que el elemento este visible despues del scroll
    WebDriverWait(selenium, 5).until(
        EC.visibility_of(user_menu)
    )
    selenium.execute_script("argument[0].click();", user_menu)
    
    # Esperar que el dropdown se abra y el boton de logout sea visible
    logout_btn = WebDriverWait(selenium, 10).until(
        EC.element_to_be_clickable((By.ID, "logout-btn"))
    )
    selenium.execute_script("arguments[0].click();", logout_btn)