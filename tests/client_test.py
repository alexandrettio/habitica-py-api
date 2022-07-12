from decouple import config

from consts import TOKEN, USER_ID, USER_NAME
from habitica.client import Client
import config as c


def test_env_config():
    """
    Checks if .env file exists and filled with correct keys
    :return:
    """
    user_id = config('habitica_user_id', default="")
    token = config('habitica_token', default="")
    assert user_id != ""
    assert token != ""


def test_auth():
    """
    This is dirty test. It depends on availability habitica.api
    :return:
    """
    user = Client(c.user1[USER_ID], c.user1[TOKEN])
    user = user.get_user_info()
    assert user.id == c.user1[USER_ID]
    assert user.username == c.user1[USER_NAME]
    assert user.party == ""
