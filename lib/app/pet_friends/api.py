import requests



class PetFriends:
    def __init__(self):
        self.url  =  'https://petfriends.skillfactory.ru'

    def get_api_key(self, email, password):
        """
        Метод авторизации, в ответе получаем api_key
        :param email: str
        :param password: str
        :return: json
        """
        headers = {
            'email': email,
            'password': password
        }
        resp = requests.get(url=self.url+'/api/key', headers=headers)
        return resp

    def get_api_pets(self, auth_key, filter = ''):
        """
        Метод получения питомцев, с авторизацией по auth_key и с необязательной фильтрацией. В ответе получаем json со
        всеми питомцами
        :param filter: str
        :param auth_key: json
        :return: json
        """
        headers = {
            'auth_key' : auth_key['key'],
        }
        resp = requests.get(url=self.url+f'/api/pets?filter={filter}', headers=headers)
        return resp

    def post_api_pets(self, auth_key, name, age, animal_type, pet_photo):
        """
        Метод добавления питомца. Авторизация по auth_key.
        :param auth_key: json
        :param name: str
        :param age: int
        :param animal_type: str
        :param pet_photo: путь до файла
        :return: json
        """
        headers = {
            'auth_key': auth_key['key'],
        }
        data = {
            'name' : name,
            'age' : age,
            'animal_type' : animal_type
        }
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
        resp = requests.post(url=self.url + '/api/pets', headers=headers, data=data, files=file)
        return resp





