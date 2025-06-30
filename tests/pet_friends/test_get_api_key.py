import pytest
from datetime import datetime

from lib import settings
from lib.app.pet_friends.api import PetFriends
from lib.constant.pet_friens_const import Kitty

pf = PetFriends()

@pytest.fixture(scope="class")
def api_key():
    resp = pf.get_api_key(email=settings.email, password=settings.password)
    return resp.json()

@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print (f"\nТест шел: {end_time - start_time}")

class TestApiKey:

    def test_get_api_key_for_valid_user(self):
        """
            Проверяем что метод GET api/key отдает 200 и длина ключа соответсвует требованиям
        """
        resp = pf.get_api_key(email=settings.email, password=settings.password)
        key = resp.json()
        assert resp.status_code == 200
        assert len(key['key']) == 56

    def test_get_pets_with_valid_key(self, api_key):
        """
            Проверяем что метод GET api/pets c валидным auth_key отдает петомцев:
            1. Получаем api-key методом GET api/key
            2. Получаем питомцев методом GET api/pets, - ожидаем код 200 и получить не пустой ответ
        """
        resp = pf.get_api_pets(auth_key=api_key, filter='')
        all_pets = resp.json()
        assert resp.status_code == 200
        assert len(all_pets['pets'])>0

    def test_post_with_valid_data(self, api_key):
        """
            Проверяем что метод POST api/pets c валидным auth_key добавляет питумца:
            1. Получаем api-key методом GET api/key
            2. Добавляем питомцев методом GET api/pets, - ожидаем код 200, в ответе соответсвует имя и возраст
        """
        resp = pf.post_api_pets(auth_key=api_key, name=Kitty.NAME, age=Kitty.AGE, animal_type=Kitty.ANIMAL_TYPE,
                                pet_photo=Kitty.FILE)
        pet_dict = resp.json()
        assert resp.status_code == 200
        assert pet_dict['age'] == Kitty.AGE
        assert pet_dict['name'] == Kitty.NAME
        assert pet_dict['animal_type'] == Kitty.ANIMAL_TYPE
