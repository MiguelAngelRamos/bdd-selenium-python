import os
import pytest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

project_root = os.path.dirname(os.path.abspath(__file__)) ## Obtiene desde la raiz del proyecto el archivo conftest.py
sys.path.insert(0, project_root)

pytest_plugins = "steps.common_steps" # Esto le dice a pytest que cargue los pasos comunes

@pytest.fixture(scope="session")
def base_url():
    # return "https://ecommerce-e2e.netlify.app"
    return os.getenv("BASE_URL", "https://ecommerce-e2e.netlify.app")


@pytest.fixture
def selenium():
    options = Options()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def reset_between_test(selenium, base_url):
    selenium.delete_all_cookies()
    selenium.get(f"{base_url}/index.html")
    yield