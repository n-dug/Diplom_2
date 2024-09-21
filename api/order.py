import allure
import requests
import helpers.constants as url


class Order:

    def __init__(self):
        self.id = None
        self.data = {}

    @allure.step('Refresh token')
    def refresh_token(self):
        # Request a new token
        refresh_token_url = f"{url.BASE_URL}{url.REFRESH_TOKEN}"
        response = requests.post(refresh_token_url)
        if response.status_code == 200:
            token = response.json()['refreshToken']  # Assuming 'token' key in the response JSON
            return token
            # Parse the response JSON to get the tokens
            # tokens = response.json()
            # access_token = tokens['accessToken']
            # refresh_token = tokens['refreshToken']
        else:
            raise Exception("Failed to refresh token")

    @allure.step('Create an order')
    def create_order(self, data):
        # Refresh the token before making the request
        token = self.refresh_token()

        # Set up the Authorization header with the new token
        headers = {'Authorization': f'Bearer {token}'}

        # Make the POST request to create the order
        url_create_order = f"{url.BASE_URL}{url.CREATE_ORDER}"
        response = requests.post(url_create_order, json=data, headers=headers)

        # Handle response and store relevant data
        if response.status_code == 200:
            self.data = self.get_order_by_track_num(self.data)
            self.id = self.get_order_id_by_track_num(self.data)
        else:
            raise Exception(f"Failed to create order: {response.status_code} {response.text}")

        return response

    # @allure.step('Create an order')
    # def create_order(self, data):
    #     url_create_order = f"{url.BASE_URL}{url.CREATE_ORDER}"
    #     headers =
    #     response = requests.post(url_create_order, json=data, headers=headers)
    #     self.track_num = response.json()['track']
    #     self.data = self.get_order_by_track_num(self.track_num)
    #     self.id = self.get_order_id_by_track_num(self.data)
    #     return response

    # @allure.step('Get an order by a track number')
    # def get_order_by_track_num(self, order_track_num):
    #     url_get_order = f"{url.BASE_URL}{url.GET_ORDER_BY_ID}?t={order_track_num}"
    #     return requests.get(url_get_order)

    # @allure.step('Get an order ID by a track number')
    # def get_order_id_by_track_num(self, data):
    #     return data.json()['order']['id']

    @allure.step('Get an order ID')
    def get_order_id(self):
        if self.id:
            return self.id
        return None

    # @allure.step('Get an order track number')
    # def get_order_track_num(self):
    #     if self.track_num:
    #         return self.track_num
    #     return None
