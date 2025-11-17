from pytest_bdd import given, when, then, parsers
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
# Mapeo de nombre de páginas a sus rutas
PAGE_ROUTES = {
    'login': '/login.html',
    'inicio': '/index.html',
    'productos': '/products.html',
    'principal': '/index.html',
    'producto': '/product.html',
    'carrito': '/cart.html',
    'checkout': '/checkout.html'
}

@given(parsers.parse('el usuario está en la página de {page_name}'))
@when(parsers.parse('el usuario navega a {page_name}'))
def navigate_to_page(selenium, base_url, page_name):
    page_name_lower = page_name.lower()
    if page_name_lower in PAGE_ROUTES:
        url = f"{base_url}{PAGE_ROUTES[page_name_lower]}"
        selenium.get(url)
    else:
        raise ValueError(f"Página {page_name} no esta definida")

@given('el usuario está en la página principal')
def usuario_en_pagina_principal(selenium, base_url):
    navigate_to_page(selenium,base_url, 'principal')

@then(parsers.parse('el usuario debería estar en la página "{page_name}"'))
def usuario_en_pagina(selenium, base_url, page_name):
    base_page = BasePage(selenium, base_url)

    expect_fragment = PAGE_ROUTES.get(page_name.lower(), page_name)
    url_did_match = base_page.wait_for_url_to_contain(expect_fragment)

    assert url_did_match, "No existe!"

@then("el localStorage debería estar vacio")
def localstorage_vacio(selenium):
    WebDriverWait(selenium, 10).until(
        lambda selenium: (
            selenium.execute_script("return localStorage.getItem('token');") in [None, "", "undefined", "null"] and
            selenium.execute_script("return localStorage.getItem('user');") in [None, "", "undefined", "null"]
        )
    )

    token = selenium.execute_script("return localStorage.getItem('token');")
    user = selenium.execute_script("return localStorage.getItem('user');")
    ## Assertions finales con mensajes descriptivos
    assert token in [None, "", "undefined", "null"], f"Token deberia estar vacio pero es: {token}"
    assert user in [None, "", "undefined", "null"], f"Token deberia estar vacio pero es: {user}"
    #TODO: Candidato para ir a los pasos comunes