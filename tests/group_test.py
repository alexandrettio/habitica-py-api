from typing import Tuple

from consts import PARTIES
from habitica import error
from habitica.client import Client
import config as c


def test_party_unable_to_join(init_users):
    """
    Unable to join party if there is no invite.
    """
    user, _ = init_users
    user_info = user.get_user_info()
    assert user_info.party == ""
    result = user.group.join(c.TARGET_PARTY)
    assert isinstance(result, error.NotAuthorizedError)
    assert result.message == "Can't join a group you're not invited to."


def test_party_invite(init_users):
    """
    Test that invitation has been sent
    """

    def tear_down(user: Client):
        reject_response = user.group.reject_invite(c.TARGET_PARTY)
        assert not isinstance(reject_response, error.HabiticaError)

    receiver, inviter = init_users
    pre_invites = receiver.get_user_info().get_invitations()
    assert len(pre_invites[PARTIES]) == 0

    invite_response = inviter.group.invite_by_uuid(receiver.user_id)
    assert not isinstance(invite_response, error.HabiticaError)

    post_invites = receiver.get_user_info().get_invitations()
    assert len(post_invites[PARTIES]) == 1
    assert post_invites[PARTIES][0].inviter == inviter.user_id
    tear_down(receiver)


def test_reject_invite(init_users):
    """User can reject existing invite."""
    def set_up() -> Client:
        receiver_user, inviter_user = init_users
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)
        return receiver_user

    receiver = set_up()
    reject_response = receiver.group.reject_invite(c.TARGET_PARTY)
    assert not isinstance(reject_response, error.HabiticaError)
    invites = receiver.get_user_info().get_invitations()
    assert len(invites[PARTIES]) == 0


def test_unable_to_join_more_than_one_group(init_users):
    """User can't join party if already has one."""

    def set_up() -> Tuple[Client, Client]:
        receiver_user, inviter_user = init_users
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


def test_successful_join(init_users):
    """Join after invite has no error if user has no party."""
    def set_up() -> Client:
        receiver_user, inviter_user = init_users
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


def test_successful_leave(init_users):
    """User can leave from his party."""
    def set_up() -> Client:
        receiver_user, inviter_user = init_users
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


def test_get_group_info(init_users):
    _, user = init_users
    info_response = user.group.get_info()
    assert not isinstance(info_response, error.HabiticaError)


def test_unable_get_group_info(init_users):
    user, _ = init_users
    info_response = user.group.get_info()
    assert isinstance(info_response, error.NotFoundError)
    assert info_response.message == "Group not found or you don't have access."


def test_create_group(init_users):
    def tear_down(user: Client):
        user.group.leave()

    group_creator, _ = init_users
    create_response = group_creator.group.create("api_test's Party", "party", "private")
    assert not isinstance(create_response, error.HabiticaError)
    info_response = group_creator.group.get_info()
    assert not isinstance(info_response, error.HabiticaError)

    tear_down(group_creator)


def test_get_groups(init_users):
    _, user = init_users
    response = user.group.get_groups("tavern,party")
    assert not isinstance(response, error.HabiticaError)
    assert len(response.data) == 2


def test_update_groups(init_users):
    def set_up() -> Client:
        group_creator, _ = init_users
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


def test_add_manager(init_users):
    def set_up() -> Tuple[Client, Client]:
        group_manager, group_owner = init_users
        group_owner.group.invite_by_uuid(group_manager.user_id)
        group_manager.group.join(group_owner.get_user_info().party)
        return group_owner, group_manager

    def tear_down(group_owner: Client, group_manager: Client):
        group_owner.group.remove_manager(group_manager.user_id)
        group_manager.group.leave()

    owner, manager = set_up()

    group_response = owner.group.get_info()

    add_manager_response = owner.group.add_manager(manager.user_id)
    assert not isinstance(add_manager_response, error.HabiticaError)

    after_group_response = owner.group.get_info()
    assert group_response != after_group_response

    tear_down(owner, manager)
