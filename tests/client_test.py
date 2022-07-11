from decouple import config
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
    habitica = Client(c.USER_ID, c.TOKEN)
    user = habitica.get_user_info()
    assert user.id == c.USER_ID
    assert user.username == c.USER_NAME
    assert user.party == ""
