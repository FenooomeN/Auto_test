from lib.app.pet_store.petstore import PetStore
from lib.constant.pet_shop_const import PetStatus

pet_store = PetStore()

class TestPet():

    def test_get_sold_pets(self, status=PetStatus.SOLD):
        """Проверяем что методом GET pet_find_by_status со параметром Sold, получаем только проданных питомцев"""
        resp = pet_store.get_pet_find_by_status(status=status)
        for r in resp.json():
            assert r['status'] == PetStatus.SOLD

