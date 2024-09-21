import allure
import helpers.constants as c
import requests


class TestCreateOrder:
    @allure.title('Order created successfully while signed in')
    def test_create_order_while_signed_in_success(self, created_user):
        response = created_user.create_user()
        token = response.json().get("accessToken")
        payload = {
            "ingredients": [c.BUN_R2_D3, c.MAIN_PROTOSTOMIA, c.SAUSE_SPICY_X]
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.post(c.BASE_URL+c.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 200
        assert c.CREATE_ORDER_SUCCESS in response.text

    @allure.title('Order created successfully while signed out')
    def test_create_order_while_signed_out_success(self):
        payload = {
            "ingredients": [c.BUN_R2_D3, c.MAIN_PROTOSTOMIA, c.SAUSE_SPICY_X]
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(c.BASE_URL+c.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 200
        assert c.CREATE_ORDER_SUCCESS in response.text

    @allure.title('Creating order with no ingredients')
    def test_create_order_no_ingredients_failure(self):
        payload = {
            "ingredients": []
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(c.BASE_URL+c.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 400
        assert c.CREATE_ORDER_WITHOUT_INGREDIENTS in response.text

    @allure.title('Creating order with wrong ingredient')
    def test_create_order_wrong_ingredient_failure(self):
        payload = {
            "ingredients": [c.BUN_R2_D3, c.MAIN_PROTOSTOMIA, c.INCORRECT_INGREDIENT]
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(c.BASE_URL+c.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 500
        assert c.CREATE_ORDER_INCORRECT_INGREDIENT in response.text
