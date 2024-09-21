import allure
import requests
import helpers.constants as url
from faker import Faker


class User:
    def __init__(self):
        self.data = None
        self.account_id = None

    @allure.step('Generate user data')
    def __generate_user_data(self):
        fake = Faker()
        data = {}
        data["name"] = fake.first_name()
        data["email"] = fake.email()
        data["password"] = fake.password()
        return data

    @allure.step('Get a email')
    def get_email(self):
        return self.data['email']

    @allure.step('Get a password')
    def get_password(self):
        return self.data['password']

    @allure.step('Get a user name')
    def get_name(self):
        return self.data['name']

    @allure.step('Get user data')
    def get_user_data(self):
        return self.data

    @allure.step('Create a user')
    def create_user(self, email: str = '', password: str = '', name: str = ''):
        if email == '' and password == '' and name == '':
            self.data = self.__generate_user_data()
        response = requests.post(f"{url.BASE_URL}{url.REGISTER_USER}", json=self.data)
        return response

    @allure.step('Login')
    def login_user(self, email: str = '', password: str = ''):
        if email == '' and password == '':
            data = {
                "email": self.get_email(),
                "password": self.get_password(),
            }
        else:
            data = {
                "email": email,
                "password": password,
            }
        return requests.post(f"{url.BASE_URL}{url.LOGIN_USER}", json=data)

    @allure.step('Delete a user')
    def delete_user(self, user_id=None):
        return requests.delete(f"{url.BASE_URL}{url.DELETE_USER}/{user_id}")

    @allure.step('Get a user ID')
    def get_user_id(self, email='', password=''):
        if email == '' and password == '':
            self.data = {
                "email": self.get_email(),
                "password": self.get_password(),
            }
        else:
            self.data = {
                "email": email,
                "password": password,
            }
        response = self.login_user(self.get_email(), self.get_password())
        if response.status_code == 200 and self.account_id is None:
            self.account_id = response.json().get('id')
            return self.account_id
        return -1
