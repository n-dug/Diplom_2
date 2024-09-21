import allure
import pytest
import helpers.constants as c


class TestSignIn:
    @allure.title('Sign in as an existed user')
    def test_login_user_success(self, created_user):
        response = created_user.login_user()
        # email is a unique field, instead of ID
        created_user.account_id = response.json().get('email')
        assert response.status_code == 200
        assert created_user.get_email() is not None

    @allure.title('Sign in using incorrect login or password')
    @pytest.mark.parametrize("key", ("email", "password"))
    def test_login_with_wrong_credentials_failure(self, created_user, key):
        created_user.data[key] = 'Unknown'
        response = created_user.login_user()
        assert response.status_code == 401 and response.json().get('message') == c.TEXT_INCORRECT_FIELD

