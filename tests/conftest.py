import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def base_url():
    return "https://ecommerce-e2e.netlify.app"

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