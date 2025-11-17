from pytest_bdd import given, when, then, parsers
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
    url_did_match = base_page
    # WebDriverWait(selenium, 15).until(
    #     lambda d: page_name in d.current_url,
    #     message=f"Esperaba estar en '{page_name} pero la URL ES: {selenium.current_url}"
    # )
    # assert page_name in selenium.current_url;
    # #TODO: Candidato para ir a los pasos Comunes