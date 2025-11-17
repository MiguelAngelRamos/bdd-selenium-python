from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.components.navbar_component import NavbarComponent

class IndexPage(BasePage):
    
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

        # 2. Composición "IndexPage tiene un NavbarComponent"
        self.navbar = NavbarComponent(self.driver, self.base_url)

   

    

