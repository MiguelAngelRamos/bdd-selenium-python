from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class IndexPage(BasePage):

    # Localizadores
    NAVBAR = (By.CSS_SELECTOR, "nav.navbar")
    PRODUCTS_LINK = (By.LINK_TEXT, "Productos")
    CART_LINK = (By.PARTIAL_LINK_TEXT, "Carrito")
    CART_COUNT = (By.ID, "mini-cart-count")
    # localizadores con condicion de login de usuario
    CHECKOUT_LINK = (By.ID, "Checkout")
    LOGOUT_BUTTON = (By.ID, "logout-btn")


    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def is_navbar_visible(self):
        return self.is_element_visible(*self.NAVBAR)
    
    def is_products_link_visible(self):
        return self.is_element_visible(*self.PRODUCTS_LINK)

    def is_cart_link_visible(self):
        return self.is_element_visible(*self.CART_LINK)

    def is_logout_button_visible(self):
        return self.is_element_visible(*self.LOGOUT_BUTTON)
    

    # Clicks 
    def click_products(self):
        self.find_clickable(*self.PRODUCTS_LINK).click()
    
    def click_cart(self):
        self.find_clickable(*self.CART_LINK).click()

    def click_logout(self):
        self.find_clickable(*self.LOGOUT_BUTTON).click()