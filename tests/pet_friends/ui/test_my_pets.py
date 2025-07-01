import re
from selenium.webdriver.common.by import By


class TestMyPets:

    def test_show_all_my_pets(self, web_browser, go_to_my_pets):
        """
        Проверяем что на странице /my_pets присутствуют все питомцы, количество соответствует счетчику
        """
        # Ищем счетчик всех питомцев
        element = web_browser.find_element(By.XPATH, '//div[contains(@class, "col-sm-4 left")]')
        text = element.text
        pets_count = re.search(r'Питомцев:\s*(\d+)', text).group(1)
        pets_count = int(pets_count)

        # Находим всех питомцев
        pets = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]//tbody/tr')

        # Проверяем что в списке присутствуют все питомцы
        assert len(pets) == pets_count, f'В списке присутствуют не все питомцы {len(pets)}, счетчик:{pets_count}'

    def test_photo_availability(self, web_browser, go_to_my_pets):
        """
        Проверяем что на странице /my_pets у половины питомцев есть фото
        """
        # Ищем счетчик всех питомцев
        element = web_browser.find_element(By.XPATH, '//div[contains(@class, "col-sm-4 left")]')
        text = element.text
        pets_count = re.search(r'Питомцев:\s*(\d+)', text).group(1)
        pets_count = int(pets_count)

        # Считаем количество питомцев с фотографией
        images = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]//img')
        count=0
        for i in range(pets_count):
            if images[i].get_attribute('src') == '':
                count += 1

        # Проверяем что не меньше чем у половины питомцев есть фото
        assert count <= pets_count//2, 'Меньше чем у половины питомцев, есть фото'

    def test_all_pets_have_name_breed_age(self, web_browser, go_to_my_pets):
        """
        Проверяем что на странице /my_pets у всех питомцев есть имя, возраст и порода.
        """
        # Собираем имена, породы и возраста питомцев
        names = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody//td[1]')
        breeds = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody//td[2]')
        ages = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody//td[3]')

        # Проверяем что у всех есть имя, порода, возраст
        for i in range(len(names)):
            name_str = names[i].text
            breed_str = breeds[i].text
            age_str = ages[i].text
            assert name_str != '', 'У питомца нет имени'
            assert breed_str != '', 'У питомца нет породы'
            assert age_str != '', 'У питомца нет возраста'

    def test_all_names_unique(self, web_browser, go_to_my_pets):
        """
        Проверяем что на странице /my_pets у всех питомцев разные имена.
        """
        # Собираем имена
        names = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody//td[1]')
        unique_names = set(names)

        # Проверяем что все питомцы имеют уникальные имена
        assert len(unique_names) == len(names), 'В списке есть повторяющиеся имена питомцев'

    def test_all_pets_unique(self, web_browser, go_to_my_pets):
        """
        Проверяем что на странице /my_pets в списке нет повторяющихся питомцев (имя, возраст и порода совпадают)
        """
        # Собираем имена, породы и возраста питомцев
        names = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody//td[1]')
        breeds = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody//td[2]')
        ages = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody//td[3]')

        # Собираем питомцев в список и проверяем что у всех есть имя, порода, возраст
        pets = []
        for i in range(len(names)):
            name_str = names[i].text
            breed_str = breeds[i].text
            age_str = ages[i].text
            pets.append((name_str, breed_str, age_str))

        # Проверяем что все питомцы уникальны
        assert len(pets) == len(set(pets)), 'В списке есть повторяющиеся питомцы'
