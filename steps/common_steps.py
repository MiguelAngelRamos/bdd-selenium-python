from pytest_bdd import given, when, then, parsers
# Mapeo de nombre de páginas a sus rutas
PAGE_ROUTES = {
    'login': '/login.html',
    'inicio': '/index.html',
    'productos': '/products.html',
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
