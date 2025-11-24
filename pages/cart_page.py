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