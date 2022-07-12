from typing import Tuple

from consts import PARTIES, TOKEN, USER_ID, PARTY
from habitica import error
from habitica.client import Client
import config as c
from habitica.group import HabiticaGroup


def test_party_unable_to_join():
    """
    Unable to join party if there is no invite.
    """
    user = Client(c.user1[USER_ID], c.user1[TOKEN])
    user_info = user.get_user_info()
    assert user_info.party == ""
    result = user.group.join(c.TARGET_PARTY)
    assert isinstance(result, error.NotAuthorizedError)
    assert result.message == "Can't join a group you're not invited to."


def test_party_invite():
    """
    Test that invitation has been sent
    """
    def set_up() -> Tuple[Client, Client]:
        inviter_user = Client(c.user2[USER_ID], c.user2[TOKEN])
        receiver_user = Client(c.user1[USER_ID], c.user1[TOKEN])
        return inviter_user, receiver_user

    def tear_down(user: Client):
        reject_response = user.group.reject_invite(c.TARGET_PARTY)
        assert not isinstance(reject_response, error.HabiticaError)

    inviter, receiver = set_up()
    pre_invites = receiver.get_user_info().get_invitations()
    assert len(pre_invites[PARTIES]) == 0

    invite_response = inviter.group.invite_by_uuid(receiver.user_id)
    assert not isinstance(invite_response, error.HabiticaError)

    post_invites = receiver.get_user_info().get_invitations()
    assert len(post_invites[PARTIES]) == 1
    assert post_invites[PARTIES][0].inviter == inviter.user_id
    tear_down(receiver)


def test_reject_invite():
    """User can reject existing invite."""
    def set_up() -> Client:
        inviter_user = Client(c.user2[USER_ID], c.user2[TOKEN])
        receiver_user = Client(c.user1[USER_ID], c.user1[TOKEN])
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)
        return receiver_user

    receiver = set_up()
    reject_response = receiver.group.reject_invite(c.TARGET_PARTY)
    assert not isinstance(reject_response, error.HabiticaError)
    invites = receiver.get_user_info().get_invitations()
    assert len(invites[PARTIES]) == 0


def test_unable_to_join_more_than_one_group():
    """User can't join party if already has one."""

    def set_up() -> Tuple[Client, Client]:
        inviter_user = Client(c.user2[USER_ID], c.user2[TOKEN])
        receiver_user = Client(c.user1[USER_ID], c.user1[TOKEN])
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)
        join_response = receiver_user.group.join(c.TARGET_PARTY)
        assert not isinstance(join_response, error.HabiticaError)
        return inviter_user, receiver_user

    def tear_down(user: Client):
        leave_response = user.group.leave()
        assert not isinstance(leave_response, error.HabiticaError)

    inviter, receiver = set_up()
    second_invite_response = inviter.group.invite_by_uuid(receiver.user_id)
    assert isinstance(second_invite_response, error.NotAuthorizedError)
    tear_down(receiver)


def test_successful_join():
    """Join after invite has no error if user has no party."""
    def set_up() -> Client:
        inviter_user = Client(c.user2[USER_ID], c.user2[TOKEN])
        receiver_user = Client(c.user1[USER_ID], c.user1[TOKEN])
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)
        return receiver_user

    def tear_down(user: Client):
        leave_response = user.group.leave()
        assert not isinstance(leave_response, error.HabiticaError)

    receiver = set_up()
    join_response = receiver.group.join(c.TARGET_PARTY)
    assert not isinstance(join_response, error.HabiticaError)
    tear_down(receiver)


def test_successful_leave():
    """User can leave from his party."""
    def set_up() -> Client:
        inviter_user = Client(c.user2[USER_ID], c.user2[TOKEN])
        receiver_user = Client(c.user1[USER_ID], c.user1[TOKEN])
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)

        post_invites = receiver_user.get_user_info().get_invitations()
        assert len(post_invites[PARTIES]) == 1
        assert post_invites[PARTIES][0].inviter == inviter_user.user_id
        group_id = post_invites[PARTIES][0].id
        join_response = receiver_user.group.join(group_id)
        assert not isinstance(join_response, error.HabiticaError)
        return receiver_user

    receiver = set_up()
    leave_response = receiver.group.leave()
    assert not isinstance(leave_response, error.HabiticaError)


def test_get_group_info():
    user = Client(c.user2[USER_ID], c.user2[TOKEN])
    info_response = user.group.get_info()
    assert not isinstance(info_response, error.HabiticaError)


def test_unable_get_group_info():
    user = Client(c.user1[USER_ID], c.user1[TOKEN])
    info_response = user.group.get_info()
    assert isinstance(info_response, error.NotFoundError)
    assert info_response.message == "Group not found or you don't have access."


def test_create_group():
    def tear_down(user: Client):
        user.group.leave()

    group_creator = Client(c.user1[USER_ID], c.user1[TOKEN])
    create_response = group_creator.group.create("api_test's Party", "party", "private")
    assert not isinstance(create_response, error.HabiticaError)
    info_response = group_creator.group.get_info()
    assert not isinstance(info_response, error.HabiticaError)

    tear_down(group_creator)


def test_get_groups():
    user = Client(c.user2[USER_ID], c.user2[TOKEN])
    response = user.group.get_groups("tavern,party")
    assert not isinstance(response, error.HabiticaError)
    assert len(response.data) == 2


def test_update_groups():
    def set_up() -> Client:
        group_creator = Client(c.user1[USER_ID], c.user1[TOKEN])
        create_response = group_creator.group.create("api_test's Party", "party", "private")
        assert not isinstance(create_response, error.HabiticaError)
        return group_creator

    def tear_down(user: Client):
        user.group.leave()

    manager = set_up()
    info_response = manager.group.get_info()
    assert not isinstance(info_response, error.HabiticaError)
    manager.group.update({"name": "New party name"})
    new_info_response = manager.group.get_info()
    assert new_info_response.data.name == "New party name"
    tear_down(manager)
