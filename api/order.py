import allure
import requests
import helpers.constants as url


class Order:

    def __init__(self):
        self.id = None
        self.data = {}

    @allure.step('Refresh token')
    def refresh_token(self):
        refresh_token_url = f"{url.BASE_URL}{url.REFRESH_TOKEN}"
        response = requests.post(refresh_token_url)
        if response.status_code == 200:
            token = response.json()['refreshToken']
            return token
        else:
            raise Exception("Failed to refresh token")

    @allure.step('Create an order')
    def create_order(self, data):
        token = self.refresh_token()
        headers = {'Authorization': f'Bearer {token}'}
        url_create_order = f"{url.BASE_URL}{url.CREATE_ORDER}"
        response = requests.post(url_create_order, json=data, headers=headers)
        return response

    @allure.step('Get an order ID')
    def get_order_id(self):
        if self.id:
            return self.id
        return None

