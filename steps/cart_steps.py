from pytest_bdd import scenarios, given, when, then, parsers
from pages.cart_page import CartPage

scenarios('../features/cart.feature')

@given('el carrito está vacío')
def carrito_vacio(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    cart_page.clear_cart_storage()
    if "cart.html" in selenium.current_url:
        selenium.refresh()

@when('el usuario navega a la página del carrito')
def navegar_a_carrito(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    cart_page.ensure_cart_ui_ready() # Navega y espera el renderizado completo

@then(parsers.parse('debería ver el mensaje "{mensaje}"'))
def ver_mensaje_carrito_vacio(selenium, base_url, mensaje):
    cart_page = CartPage(selenium, base_url)
    page_text = cart_page.get_body_text_lower()
    assert mensaje.lower() in page_text, f'No se encontró el mensaje esperado: {mensaje}'

