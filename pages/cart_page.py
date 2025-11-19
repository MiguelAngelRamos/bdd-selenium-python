from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    # Localizadores
    # //*[@id="cart-table"]/div
    # por clase css #cart-table .alert.alert-info
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#cart-table .alert.alert-info")

    CART_TABLE = (By.ID, "cart-table")
    CART_ROWS = (By.CSS_SELECTOR, "#cart-table tbody tr")
    CART_FOOTER = (By.CSS_SELECTOR, "#cart-table tfoot")
   

