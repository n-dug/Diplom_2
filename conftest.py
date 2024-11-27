import pytest

from api.user import User


@pytest.fixture()
def created_user():
    user = User()
    user.create_user()
    yield user
    user.delete_user(user.get_user_id())
