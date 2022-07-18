from typing import Tuple

import pytest

import consts
from consts import TOKEN, USER_ID
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
def quest_cancel():
    user1, user2 = _init_users()
    yield user1, user2
    user1.group.quest.cancel()


@pytest.fixture
def invite():
    user1, user2 = _init_users()
    user2.group.invite_by_uuid(user1.user_id)
    yield user1, user2


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


@pytest.fixture
def group_create():
    user1, user2 = _init_users()
    user1.group.create(
        "api_test's Party", consts.GroupType.PARTY, consts.Privacy.PRIVATE
    )
    yield user1, user2
