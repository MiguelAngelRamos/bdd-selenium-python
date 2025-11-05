from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pytest

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
       
    def open(self, url: str) -> None:
        self.driver.get(url)
    
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
            WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False