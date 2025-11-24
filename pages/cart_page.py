from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.components.navbar_component import NavbarComponent

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



