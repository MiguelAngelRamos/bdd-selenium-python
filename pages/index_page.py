from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class IndexPage(BasePage):

    # Localizadores
    
    CART_COUNT = (By.ID, "mini-cart-count")
    # localizadores con condicion de login de usuario
    CHECKOUT_LINK = (By.ID, "Checkout")
    LOGOUT_BUTTON = (By.ID, "logout-btn")


    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

   
    


    def is_logout_button_visible(self):
        return self.is_element_visible(*self.LOGOUT_BUTTON)
    

