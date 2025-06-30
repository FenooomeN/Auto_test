import time
from selenium.webdriver.common.by import By
from lib import settings


class TestAuth:

    def test_auth(self, web_browser):
        """Проверяем авторизацию на сайте PetFriends"""
        web_browser.get('https://petfriends.skillfactory.ru/')

        buttom_reg = web_browser.find_element(By.CSS_SELECTOR, ".btn.btn-success")
        buttom_reg.click()

        buttom_alredy_reg = web_browser.find_element(By.XPATH, "//a[text()='У меня уже есть аккаунт']")
        buttom_alredy_reg.click()

        field_email = web_browser.find_element(By.ID, 'email')
        field_email.clear()
        field_email.send_keys(settings.email)
        field_password = web_browser.find_element(By.ID, 'pass')
        field_password.clear()
        field_password.send_keys(settings.password)
        buttom_submit = web_browser.find_element(By.CSS_SELECTOR, ".btn.btn-success")
        buttom_submit.click()

        time.sleep(1)
        assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',  \
            f"login error {web_browser.current_url}"
