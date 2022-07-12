from typing import Tuple

from consts import PARTIES, TOKEN, USER_ID, PARTY
from habitica import error
from habitica.client import Client
import config as c


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
        # print(invite_response["data"][0]["id"])
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
