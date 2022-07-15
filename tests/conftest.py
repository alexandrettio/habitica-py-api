from typing import Tuple

import pytest

from consts import USER_ID, TOKEN
from habitica.client import Client
from tests import config


def _init_users() -> Tuple[Client, Client]:
    user1 = Client(config.user1[USER_ID], config.user1[TOKEN])
    user2 = Client(config.user2[USER_ID], config.user2[TOKEN])
    return user1, user2


@pytest.fixture(scope="session")
def init_users():
    yield _init_users()


@pytest.fixture
def group_leave():
    user1, user2 = _init_users()
    yield user1, user2
    user1.group.leave()


@pytest.fixture
def reject_invite():
    user1, user2 = _init_users()
    yield user1, user2
    user1.group.reject_invite(user2.get_user_info().party)


@pytest.fixture
def join_group():
    user1, user2 = _init_users()
    user2.group.invite_by_uuid(user1.user_id)
    user1.group.join(user2.get_user_info().party)
    yield user1, user2


@pytest.fixture
def remove_manager():
    user1, user2 = _init_users()
    yield user1, user2

    user2.group.remove_manager(user1.user_id)
