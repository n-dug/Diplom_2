import allure
import helpers.constants as c
import requests
from faker import Faker


class TestUpdateData:
    @allure.title('Change email while authorized')
    def test_change_email_while_authorized_success(self, created_user):
        response = created_user.create_user()
        token = response.json().get("accessToken")
        fake = Faker()
        payload = {
            "email": fake.email()
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.patch(c.BASE_URL+c.UPDATE_DATA, headers=headers, json=payload)
        assert response.status_code == 200
        assert c.UPDATE_USER in response.text

    @allure.title('Change password while authorized')
    def test_change_password_while_authorized_success(self, created_user):
        response = created_user.create_user()
        token = response.json().get("accessToken")
        fake = Faker()
        payload = {
            "password": fake.password()
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.patch(c.BASE_URL+c.UPDATE_DATA, headers=headers, json=payload)
        assert response.status_code == 200
        assert c.UPDATE_USER in response.text

    @allure.title('Change name while authorized')
    def test_change_name_while_authorized_success(self, created_user):
        response = created_user.create_user()
        token = response.json().get("accessToken")
        fake = Faker()
        payload = {
            "name": fake.first_name()
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.patch(c.BASE_URL+c.UPDATE_DATA, headers=headers, json=payload)
        assert response.status_code == 200
        assert c.UPDATE_USER in response.text

    @allure.title('Change email and password while unauthorized')
    def test_update_credentials_unauthorized(self):
        fake = Faker()
        payload = {
            "email": fake.email(),
            "password": fake.password()
        }
        headers = {"Content-type": "application/json"}
        response = requests.patch(c.BASE_URL+c.UPDATE_DATA, headers=headers, json=payload)
        assert response.status_code == 401
        assert c.UPDATE_USER_UNSUCCESSFULLY in response.text
