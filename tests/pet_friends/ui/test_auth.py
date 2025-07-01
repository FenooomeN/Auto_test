from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib import settings


class TestAuth:

    def test_auth(self, web_browser):
        """Проверяем авторизацию на сайте PetFriends"""
        # Нажимаем кнопку "Зарегистрироваться"
        web_browser.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

        # Нажимаем кнопку "У меня уже есть аккаунт"
        web_browser.find_element(By.XPATH, "//a[text()='У меня уже есть аккаунт']").click()

        # Вводим логин и пароль и нажимаем кнопку "Войти"
        web_browser.find_element(By.ID, 'email').send_keys(settings.email)
        web_browser.find_element(By.ID, 'pass').send_keys(settings.password)
        web_browser.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

        # Проверяем что мы на странице /all_pets
        WebDriverWait(web_browser, 10).until(EC.title_is('PetFriends: My Pets'))
        assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "login error"
