import allure
import helpers.constants as c
import pytest


class TestSignUp:
    @allure.title('Sign up as a unique user')
    def test_create_unique_user_success(self, created_user):
        response = created_user.create_user()
        assert response.status_code == 200
        assert c.CREATE_USER_SUCCESS in response.text

    @allure.title('Sign up a user twice')
    def test_create_user_twice_failure(self, created_user):
        response = created_user.create_user(
            created_user.get_email(), created_user.get_password(), created_user.get_name()
        )
        assert response.status_code == 403
        assert response.json().get('message') == c.TEXT_USER_EXISTS

    @allure.title('Sign up without an essential field')
    @pytest.mark.parametrize("key", ["email", "password", "name"])
    def test_create_user_without_login_or_password_failure(self, created_user, key):
        created_user.data[key] = None
        response = created_user.create_user(name="NoLoginPass")
        assert response.status_code == 403
        assert response.json().get('message') == c.TEXT_EMPTY_FIELD


