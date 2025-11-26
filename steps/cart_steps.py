from pytest_bdd import scenarios, given, when, then, parsers
from pages.cart_page import CartPage

scenarios('../features/cart.feature')

@given('el carrito está vacío')
def carrito_vacio(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    cart_page.clear_cart_storage()
    if "cart.html" in selenium.current_url:
        selenium.refresh()

@given('el usuario tiene un producto en el carrito')
def usuario_tiene_producto(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    cart_page.add_test_product()
    if "cart.html" in selenium.current_url:
        selenium.refresh()


@when('el usuario navega a la página del carrito')
def navegar_a_carrito(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    cart_page.ensure_cart_ui_ready() # Navega y espera el renderizado completo

@when('el usuario hace clic en "{button_text}"')
def click_en_boton(selenium, base_url, button_text):
    cart_page = CartPage(selenium, base_url)
    cart_page.ensure_cart_ui_ready() # Asegura que la UI esté lista
    cart_page.click_button_by_text(button_text)




@then(parsers.parse('debería ver el mensaje "{mensaje}"'))
def ver_mensaje_carrito_vacio(selenium, base_url, mensaje):
    cart_page = CartPage(selenium, base_url)
    page_text = cart_page.get_body_text_lower()
    assert mensaje.lower() in page_text, f'No se encontró el mensaje esperado: {mensaje}'

@given('el usuario ha agregado un producto al carrito')
def usuario_agrego_producto(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    sample_product = [
        {
            "id": 1,
            "title": "Essence Mascara Lash Princess",
            "price": 9.99,
            "thumbnail":"https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/thumbnail.webp",
            "qty": 1
        }
    ]
    cart_page.inject_product_to_storage(sample_product)

@when('el usuario navega a la página del carrito')
def navegar_a_carrito(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    cart_page.ensure_cart_ui_ready() # Navega y espera el renderizado completo

@then('debería ver el producto en la lista')
def verificar_producto_lista(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    assert cart_page.get_items_count() > 0, "No hay productos en el carrito"

@then('debería ver el total calculado')
def verificar_total(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    total_text = cart_page.get_total_text()
    # Buscamos indicadores de total en el texto
    assert "total" in total_text.lower() or "$" in total_text, "El total no es visible"

@then('el producto debería eliminarse del carrito')
def verificar_producto_eliminado(selenium, base_url):
    cart_page = CartPage(selenium, base_url)
    is_empty = "vacío" in cart_page.get_body_text_lower() or cart_page.get_items_count() == 0
    assert is_empty, "El carrito no está vacío después de eliminar el producto"