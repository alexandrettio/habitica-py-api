from typing import Tuple
from uuid import UUID

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


def test_party_invite(reject_invite):
    """
    Test that invitation has been sent
    """
    receiver, inviter = reject_invite
    pre_invites = receiver.get_user_info().get_invitations()
    assert len(pre_invites[PARTIES]) == 0

    invite_response = inviter.group.invite_by_uuid(receiver.user_id)
    assert not isinstance(invite_response, error.HabiticaError)

    post_invites = receiver.get_user_info().get_invitations()
    assert len(post_invites[PARTIES]) == 1
    assert post_invites[PARTIES][0].inviter == inviter.user_id


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


def test_unable_to_join_more_than_one_group(group_leave):
    """User can't join party if already has one."""
    def set_up() -> Tuple[Client, Client]:
        receiver_user, inviter_user = group_leave
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)
        join_response = receiver_user.group.join(c.TARGET_PARTY)
        assert not isinstance(join_response, error.HabiticaError)
        return inviter_user, receiver_user

    inviter, receiver = set_up()
    second_invite_response = inviter.group.invite_by_uuid(receiver.user_id)
    assert isinstance(second_invite_response, error.NotAuthorizedError)


def test_successful_join(group_leave):
    """Join after invite has no error if user has no party."""
    def set_up() -> Client:
        receiver_user, inviter_user = group_leave
        invite_response = inviter_user.group.invite_by_uuid(receiver_user.user_id)
        assert not isinstance(invite_response, error.HabiticaError)
        return receiver_user

    receiver = set_up()
    join_response = receiver.group.join(c.TARGET_PARTY)
    assert not isinstance(join_response, error.HabiticaError)


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
    info = user.group.get_info()
    assert not isinstance(info, error.HabiticaError)
    assert info.data.id == UUID(c.TARGET_PARTY)


def test_unable_get_group_info(init_users):
    user, _ = init_users
    info_response = user.group.get_info()
    assert isinstance(info_response, error.NotFoundError)
    assert info_response.message == "Group not found or you don't have access."


def test_create_group(group_leave):
    group_creator, _ = group_leave
    create_response = group_creator.group.create("api_test's Party", "party", "private")
    assert not isinstance(create_response, error.HabiticaError)
    info_response = group_creator.group.get_info()
    assert not isinstance(info_response, error.HabiticaError)


def test_get_groups(init_users):
    _, user = init_users
    response = user.group.get_groups("tavern,party")
    assert not isinstance(response, error.HabiticaError)
    assert len(response.data) == 2


def test_update_groups(group_leave):
    def set_up() -> Client:
        group_creator, _ = group_leave
        create_response = group_creator.group.create("api_test's Party", "party", "private")
        assert not isinstance(create_response, error.HabiticaError)
        return group_creator

    manager = set_up()
    info_response = manager.group.get_info()
    assert not isinstance(info_response, error.HabiticaError)
    new_name = "New party name"
    manager.group.update({"name": new_name})
    new_info = manager.group.get_info()
    assert new_info.data.name == new_name


def test_add_manager(join_group, remove_manager, group_leave):
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
    after_group = owner.group.get_info()
    assert len(group_before.data.managers) < len(after_group.data.managers)
