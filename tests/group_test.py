from typing import Tuple

from consts import PARTIES, TOKEN, USER_ID
from habitica import error
from habitica.client import Client
import config as c


def test_party_unable_to_join():
    """
    Unable to join party if there is no invite.
    :return:
    """
    user = Client(c.user1[USER_ID], c.user1[TOKEN])
    user_info = user.get_user_info()
    assert user_info.party == ""
    result = user.group.join(c.TARGET_PARTY)
    assert isinstance(result, error.NotFoundError)
    assert result.message == "Not found."


def test_party_invite():
    """
    Test that invitation has been sent
    :return:
    """
    def tear_down(user: Client):
        reject_response = user.group.reject_invite(c.TARGET_PARTY)
        assert not isinstance(reject_response, error.HabiticaError)

    def set_up() -> Tuple[Client, Client]:
        inviter_user = Client(c.user2[USER_ID], c.user2[TOKEN])
        receiver_user = Client(c.user1[USER_ID], c.user1[TOKEN])
        return inviter_user, receiver_user

    inviter, receiver = set_up()
    pre_invites = receiver.get_user_info().get_invitations()
    assert len(pre_invites[PARTIES]) == 0

    invite_response = inviter.group.invite(c.user1[USER_ID])
    assert not isinstance(invite_response, error.HabiticaError)

    post_invites = receiver.get_user_info().get_invitations()
    assert len(post_invites[PARTIES]) == 1
    assert post_invites[PARTIES][0].inviter == inviter.user_id
    tear_down(receiver)
