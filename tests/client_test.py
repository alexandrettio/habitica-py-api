import config as c
import pytest
from decouple import config

from consts import USER_ID, USER_NAME


@pytest.mark.local
def test_env_config():
    """
    Checks if .env file exists and filled with correct keys
    :return:
    """
    user_id = config("habitica_user_id", default="")
    token = config("habitica_token", default="")
    assert user_id != ""
    assert token != ""


def test_auth(sleep_a_bit, init_users):
    """
    This is dirty test. It depends on availability habitica.api
    :return:
    """
    authed_user, _ = init_users
    user = authed_user.user.get_user_info().data
    assert str(user.id) == c.user1[USER_ID]
    assert user.auth.local.username == c.user1[USER_NAME]
    assert user.party.id is None
