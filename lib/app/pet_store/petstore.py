import requests

class PetStore:
    
    def __init__(self):
        self.url = 'https://petstore.swagger.io'


    def get_pet_find_by_status(self, status):
        resp = requests.get(f'{self.url}/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})
        return resp

