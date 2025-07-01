import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib import settings

@pytest.fixture(autouse=True)
def web_browser(request, selenium):
    """Открытие браузера"""
    browser = selenium
    browser.set_window_size(1400, 1000)
    browser.get('https://petfriends.skillfactory.ru/')

    yield browser

    browser.quit()

@pytest.fixture
def go_to_my_pets(web_browser):
    # Нажимаем кнопку "Зарегистрироваться"
    web_browser.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

    # Нажимаем кнопку "У меня уже есть аккаунт"
    WebDriverWait(web_browser, 10).until(EC.title_is('PetFriends: New User'))
    web_browser.find_element(By.XPATH, "//a[text()='У меня уже есть аккаунт']").click()

    # Вводим логин и пароль и нажимаем кнопку "Войти"
    WebDriverWait(web_browser, 10).until(EC.title_is('PetFriends: Login'))
    web_browser.find_element(By.ID, 'email').send_keys(settings.email)
    web_browser.find_element(By.ID, 'pass').send_keys(settings.password)
    web_browser.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

    # Нажимаем кнопку "Мои питомцы"
    WebDriverWait(web_browser, 10).until(EC.title_is('PetFriends: My Pets'))
    button_my_pets = web_browser.find_element(By.LINK_TEXT, "Мои питомцы")
    button_my_pets.click()
