from habitica import error
from habitica.client import Client
import config as c
from habitica.party import Party


def test_party_unable_to_join():
    """
    Unable to join party if there is no invite.
    :return:
    """
    user = Client(c.user1["USER_ID"], c.user1["TOKEN"])
    user_info = user.get_user_info()
    assert user_info.party == ""
    party = Party(c.user1["USER_ID"], c.user1["TOKEN"])
    result = party.join(c.TARGET_PARTY)
    assert isinstance(result, error.NotFoundError)
    assert result.message == "Not found."


def test_party_invite():
    def tear_down():
        receiver = Party(c.user1["USER_ID"], c.user1["TOKEN"])
        reject_response = receiver.reject_invite(c.TARGET_PARTY)
        assert not isinstance(reject_response, error.HabiticaError)

    inviter = Party(c.user2["USER_ID"], c.user2["TOKEN"])
    invite_response = inviter.invite(c.user1["USER_ID"])
    assert not isinstance(invite_response, error.HabiticaError)
    tear_down()
