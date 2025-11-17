from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class NavbarComponent(BasePage):
    """
    Este componente va encapsular toda la lógica de la barra de navegación.
    """
    # -- Localizadores del componente -- 
    NAVBAR = (By.CSS_SELECTOR, "nav.navbar")
    PRODUCTS_LINK = (By.LINK_TEXT, "Productos")
    CART_LINK = (By.PARTIAL_LINK_TEXT, "Carrito")

    # -- Localizadores del estado "logueado"
    USER_MENU_DROPDOWN = (By.ID, "user-name")
    LOGOUT_BUTTON = (By.ID, "logout-btn")

    # localizador del menú responsive
    NAVBAR_TOGGLER = (By.CLASS_NAME, "navbar-toggler") # eL botón de hamburguesa

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    #-- Métodos de visibilidad -- 
    def is_navbar_visible(self):
        return self.is_element_visible(*self.NAVBAR)
    
    def is_products_link_visible(self):
        return self.is_element_visible(*self.PRODUCTS_LINK)

    def is_cart_link_visible(self):
        return self.is_element_visible(*self.CART_LINK)
    

    # -- Métodos de Acción (Clicks) --
    def _click_navbar_link(self, link_locator):
        """ 
        Método privado que nos va permitir dar click en los enlaces del navbar
        """
        ## 1. Manejar el menu de hamburguesa (responsive)
    
        try:
            toggler = self.driver.find_element(*self.NAVBAR_TOGGLER)
            # Si el boton de hamburgesa es visible, en navbar esta calapsado y necesitamos expandirlo
            if toggler.is_displayed():
                toggler.click()
                # Esperar a que se el menu se expanda(espera explicita)
                # Esperar a que el enlace este visible despues de abrir el menu
                self.wait.until(EC.visibility_of_element_located(link_locator))
        except NoSuchElementException:
            # EL toggler no visible es por que estamos en (modo escritorio), continuar
            pass

        # Esto garantiza que el elemento es existe en el DOM y está en un estado que permite interacción
        element = self.find_clickable(*link_locator)
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.visibility_of(element))
        self.driver.execute_script("arguments[0].click();", element)


    # Clicks 
    def click_products(self):
        self._click_navbar_link(self.PRODUCTS_LINK)


    def click_cart(self):
        self._click_navbar_link(self.CART_LINK)

    def click_logout(self):
      
        user_menu = self.find_clickable(*self.USER_MENU_DROPDOWN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", user_menu)
        # Esperar a que el elemento este visible despues del scroll

        self.wait.until(EC.visibility_of(user_menu))
        self.driver.execute_script("arguments[0].click();", user_menu)

        # Esperar que el dropdown se abra y el boton de logout sea visible
        logout_btn = self.find_clickable(*self.LOGOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", logout_btn)
    