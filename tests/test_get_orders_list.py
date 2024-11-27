import allure
import requests
import helpers.constants as c


class TestGetOrdersInfo:
    @allure.title('Get order info while authorized')
    def test_get_order_authorized_success(self, created_user):
        response = created_user.create_user()
        token = response.json().get("accessToken")
        payload = {
            "ingredients": [c.BUN_R2_D3, c.MAIN_PROTOSTOMIA, c.SAUSE_SPICY_X]
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.post(c.BASE_URL+c.CREATE_ORDER, headers=headers, json=payload)
        response = requests.get(c.BASE_URL+c.GET_ORDER, headers=headers, json=payload)
        assert response.status_code == 200
        assert c.GET_ORDER_SUCCESS in response.text

    @allure.title('Get order info while not authorized')
    def test_get_order_no_authorization_failure(self):
        headers = {"Content-type": "application/json"}
        response = requests.get(c.BASE_URL+c.GET_ORDER, headers=headers)
        assert response.status_code == 401
        assert c.GET_ORDER_WITHOUT_AUTH in response.text
