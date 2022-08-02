from typing import Tuple
from uuid import UUID

import config as c
import pytest

from consts import GroupType, Privacy
from habitica import error
from habitica.client import Client


def test_party_unable_to_join(sleep_a_bit, init_users):
    """
    Test unable to join party if there is no invite.

    :param init_users: fixture inits users.
    :return:
    """
    user, _ = init_users
    user_info = user.user.get_user_info()
    assert user_info.data.party.id is None
    try:
        user.group.join(c.TARGET_PARTY)
    except error.NotAuthorizedError as e:
        assert e.message == "Can't join a group you're not invited to."


def test_party_invite(sleep_a_bit, reject_invite):
    """
    Test that invitation has been sent.

    :param reject_invite: fixture rejects invite to users group after test.
    :return:
    """
    receiver, inviter = reject_invite
    pre_invites = receiver.user.get_user_info().data.invitations
    assert len(pre_invites.parties) == 0

    invite_response = inviter.group.invite_by_uuid(receiver.user_id)
    assert not isinstance(invite_response, error.HabiticaError)
    assert len(invite_response.data) == 1
    assert str(invite_response.data[0].inviter) == inviter.user_id

    post_invites = receiver.user.get_user_info().data.invitations
    assert len(post_invites.parties) == 1
    assert post_invites.parties[0].get("inviter") == inviter.user_id


def test_reject_invite(sleep_a_bit, invite):
    """User can reject existing invite.

    :param invite: fixture invites users1 to user2 group before test.
    :return:
    """

    receiver, _ = invite
    reject_response = receiver.group.reject_invite(c.TARGET_PARTY)
    assert not isinstance(reject_response, error.HabiticaError)
    invites = receiver.user.get_user_info().data.invitations
    assert len(invites.parties) == 0


def test_unable_to_join_more_than_one_group(sleep_a_bit, group_leave):
    """User can't join party if already has one.

    :param group_leave: fixture leaves group by user1 after test.
    :return:"""

    def set_up() -> Tuple[Client, Client]:
        receiver_user, inviter_user = group_leave
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)
        join_response = receiver_user.group.join(c.TARGET_PARTY)
        assert not isinstance(join_response, error.HabiticaError)
        return inviter_user, receiver_user

    inviter, receiver = set_up()
    try:
        inviter.group.invite_by_uuid(receiver.user_id)
    except error.NotAuthorizedError:
        pass


def test_successful_join(sleep_a_bit, group_leave):
    """Join after invite has no error if user has no party.

    :param group_leave: fixture leaves group by user1 after test.
    :return:"""

    def set_up() -> Client:
        receiver_user, inviter_user = group_leave
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)
        return receiver_user

    receiver = set_up()
    join_response = receiver.group.join(c.TARGET_PARTY)
    assert not isinstance(join_response, error.HabiticaError)


def test_successful_leave(sleep_a_bit, init_users):
    """User can leave from his party.

    :param init_users: fixture inits users.
    :return:"""

    def set_up() -> Client:
        receiver_user, inviter_user = init_users
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)
        post_invites = receiver_user.user.get_user_info().data.invitations
        assert len(post_invites.parties) == 1
        assert post_invites.parties[0].get("inviter") == inviter_user.user_id
        group_id = post_invites.parties[0].get("id")
        join_response = receiver_user.group.join(group_id)
        assert not isinstance(join_response, error.HabiticaError)
        return receiver_user

    receiver = set_up()
    leave_response = receiver.group.leave()
    assert not isinstance(leave_response, error.HabiticaError)


def test_get_group_info(sleep_a_bit, init_users):
    """
    Test checks group info fields.
    TODO: add stub to check all test group fields are available.

    :param init_users: fixture inits users.
    :return:
    """
    _, user = init_users
    info = user.group.get_info()
    assert not isinstance(info, error.HabiticaError)
    assert info.data.id == UUID(c.TARGET_PARTY)


def test_unable_get_group_info(sleep_a_bit, init_users):
    """
    User with no party can not get group info.
    TODO: Should be fixed to check errors new class.

    :param init_users: fixture inits users.
    :return:
    """
    user, _ = init_users
    try:
        user.group.get_info()
    except error.NotFoundError as e:
        assert e.message == "Group not found or you don't have access."


def test_create_group(sleep_a_bit, group_leave):
    """
    User with no active party can create new party.

    :param group_leave: user1 leaves group owned by user1.
    :return:
    """
    party_name = "api_test's Party"
    group_creator, _ = group_leave
    create_response = group_creator.group.create(
        party_name, GroupType.PARTY, Privacy.PRIVATE
    )
    assert not isinstance(create_response, error.HabiticaError)
    assert create_response.data.name == party_name
    assert create_response.data.privacy == Privacy.PRIVATE
    assert create_response.data.group_type == GroupType.PARTY
    assert str(create_response.data.leader.secret_id) == group_creator.user_id


@pytest.mark.parametrize(
    "group_types, result", [("tavern,party", 2), ("party", 1), ("tavern", 1)]
)
def test_get_groups(sleep_a_bit, group_types, result, init_users):
    """
    Test that user2 has different amount of groups if different types of groups are given

    :param group_types: str of group types should be shown split by comma.
    :param result: int - amount of groups for current group types.
    :param init_users: fixture inits users.
    :return:
    """
    _, user = init_users
    response = user.group.get_groups(group_types)
    assert not isinstance(response, error.HabiticaError)
    assert len(response.data) == result


def test_update_groups(sleep_a_bit, group_create, group_leave):
    """
    Test user can update his own group info.
    TODO: parametrize test.

    :param group_create: fixture user1 creates group.
    :param group_leave: user1 leaves group owned by user2.
    :return:
    """
    manager, _ = group_create
    new_name = "New party name"
    updated = manager.group.update({"name": new_name})
    assert not isinstance(updated, error.HabiticaError)
    assert updated.data.name == new_name


def test_add_manager(sleep_a_bit, join_group, remove_manager, group_leave):
    """
    Test that user can add new manager in his group.

    :param join_group: fixture user1 joins group owned by user2.
    :param remove_manager: fixture user2 removes managers role user1.
    :param group_leave: user1 leaves group owned by user2.
    :return:
    """
    manager, owner = join_group

    group_before = owner.group.get_info()
    add_manager = owner.group.add_manager(manager.user_id)
    assert not isinstance(add_manager, error.HabiticaError)
    assert add_manager.data.managers.get(manager.user_id)
    group_after = owner.group.get_info()
    assert len(group_before.data.managers) < len(group_after.data.managers)
