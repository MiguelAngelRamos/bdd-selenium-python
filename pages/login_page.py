from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "username") 
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    USER_MENU = (By.ID, "user-menu")
    LOGIN_BTN = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message, .alert-danger, #error")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)
    
    def open(self):
        self.visit("login.html")
    
    def enter_username(self, username):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
    
    def click_login_button(self):
        self.find_clickable(*self.LOGIN_BUTTON).click()

    #user-menu

    def is_user_menu_visible(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.USER_MENU))
            return element.is_displayed()
        except:
            return False


    def login(self, username, password):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        