from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "username") 
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)
    
    def open(self):
        self.visit("login.html")
        
    def login(self, username, password):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.find_clickable(*self.LOGIN_BUTTON).click()