from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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