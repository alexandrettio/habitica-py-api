from typing import Tuple

import pytest

from consts import USER_ID, TOKEN
from habitica.client import Client
from tests import config


@pytest.fixture(scope="session")
def init_users() -> Tuple[Client, Client]:
    user1 = Client(config.user1[USER_ID], config.user1[TOKEN])
    user2 = Client(config.user2[USER_ID], config.user2[TOKEN])
    yield user1, user2


@pytest.fixture
def group_leave():
    user1 = Client(config.user1[USER_ID], config.user1[TOKEN])
    user2 = Client(config.user2[USER_ID], config.user2[TOKEN])
    yield user1, user2
    user1.group.leave()


@pytest.fixture
def reject_invite():
    user1 = Client(config.user1[USER_ID], config.user1[TOKEN])
    user2 = Client(config.user2[USER_ID], config.user2[TOKEN])
    yield user1, user2
    user1.group.reject_invite(user2.get_user_info().party)
