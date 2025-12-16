import pytest
import requests
from selenium import webdriver


@pytest.fixture(scope="session")
def app_url():
    """Возвращает URL приложения"""
    return "http://localhost:8080"


@pytest.fixture(scope="function")
def driver():
    """Настраивает браузер Selenium'a."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def api_session(app_url):
    """Создает заголовок для API-запроса."""
    headers = {
        "Content-Type": "application/json"
    }

    session = requests.Session()
    session.headers.update(headers)

    yield session

    session.close()