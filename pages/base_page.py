from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pytest

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = base_url
       
    def visit(self, url_path=""):
        self.driver.get(f"{self.base_url}/{url_path}")
    
    def find_element(self, by, value):
        return self.wait.until(
            EC.presence_of_element_located((by, value))
        )
    
    def find_clickable(self, by, value):
        return self.wait.until(
            EC.element_to_be_clickable((by, value))
        )
    
    def is_element_visible(self, by, value, timeout=10):
        try:
            # Usamos un wait temporal si el timeout es diferente
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False