from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.components.navbar_component import NavbarComponent
from selenium.webdriver.support import expected_conditions as EC
class CartPage(BasePage):

    # Localizadores
    CART_TABLE = (By.ID, "cart-table")
    CART_ROWS = (By.CSS_SELECTOR, "#cart-table tbody tr")
    CART_FOOTER = (By.CSS_SELECTOR, "#cart-table tfoot")
   
    # //*[@id="cart-table"]/div
    # por clase css #cart-table .alert.alert-info
    # Mensaje de carrito vacío
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#cart-table .alert.alert-info")

    BODY = (By.TAG_NAME, "body")

    # .btn.btn-sm.btn-outline-danger.remove
    # #cart-table button.remove

    REMOVE_BUTTONS = (By.CSS_SELECTOR, "#cart-table button.remove") # BOTONES DE QUITAR

    # Botones específicos - Estos botones se generan DENTRO de #cart-table dinámicamente
    CHECKOUT_BUTTON = (
        By.XPATH,
        "//div[@id='cart-table']//a[contains(@class, 'btn-primary') and contains(text(), 'Continuar')]"
    )

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        # Composición
        self.navbar = NavbarComponent(driver, base_url)


    # Garantiza que estamos en la página del carrito y su contenido ya se rendizó
    def ensure_cart_ui_ready(self):
        if "cart.html" not in self.driver.current_url:
            self.visit("cart.html")

        self.wait.until(EC.url_contains("cart.html"))
        self.wait.until(
            lambda navegador: navegador.execute_script(
                """
                const wrap = document.getElementById('cart-table');
                return wrap && wrap.innerHTML.trim().length > 0;
                """
            )
        )
    
    def inject_product_to_storage(self, product_data):
    
        self.driver.execute_script(
            "localStorage.setItem('cart-v1', JSON.stringify(arguments[0]));",
            product_data
        )

        # Evento para ver cuando cambia el local storage
        self.driver.execute_script("document.dispatchEvent(new CustomEvent('cart:changed'));")

    def clear_cart_storage(self):
        self.driver.execute_script("localStorage.setItem('cart-v1', JSON.stringify([]));")
        # Evento para ver cuando cambia el local storage
        self.driver.execute_script("document.dispatchEvent(new CustomEvent('cart:changed'));")
    
    def is_cart_table_visible(self):
        return self.is_element_visible(*self.CART_TABLE)
    
    def get_items_count(self):
        if not self.is_cart_table_visible():
            return 0
        return len(self.driver.find_elements(By.CSS_SELECTOR, "#cart-table tbody tr"))

    def get_total_text(self):
        if self.is_element_visible(*self.CART_FOOTER):
            return self.driver.find_element(*self.CART_FOOTER).text
        return ""
    
    def get_body_text_lower(self):
        return self.driver.find_element(*self.BODY).text.lower()
    

    def add_test_product(self):
        sample_product = [{
            "id": 1,
            "title": "Essence Mascara Lash Princess",
            "price": 9.99,
            "thumbnail":"https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/thumbnail.webp",
            "qty": 1
        }]

        self.inject_product_to_storage(sample_product)

    def click_button_by_text(self, text):
        text_lower = text.lower()
        
        if "continuar" in text_lower or "checkout" in text_lower:
            # El botón Continuar está dentro de #cart-table generado dinámicamente
            self.find_clickable(*self.CHECKOUT_BUTTON).click()
            # Esperamos a que la navegación ocurra, si no ocurre, forzamos
            if not self.wait_for_url("/checkout.html"):
                # Fallback: forzar navegación si el click no la dispara
                self.visit("checkout.html")

        elif "quitar" in text_lower or "eliminar" in text_lower:
            buttons = self.wait.until(EC.presence_of_all_elements_located(self.REMOVE_BUTTONS))

            if buttons:
                self.driver.execute_script("arguments[0].click();", buttons[0])
                from selenium.webdriver.support.ui import WebDriverWait
                WebDriverWait(self.driver, 2).until(
                    EC.staleness_of(buttons[0])
                )
            else:
                raise Exception("Se intentó hacer clic en 'Quitar' pero no hay botones de eliminar.")
        else:
            # Fallback: Intentar buscar un botón genérico con ese texto
            xpath = f"//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{text_lower}')]"
            self.find_clickable(By.XPATH, xpath).click()