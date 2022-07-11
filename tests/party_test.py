from habitica import error
from habitica.client import Client
import config as c
from habitica.party import Party


def test_party_unable_to_join():
    """
    Unable to join party if there is no invite.
    :return:
    """
    user = Client(c.USER_ID, c.TOKEN)
    user_info = user.get_user_info()
    assert user_info.party == ""
    party = Party(c.USER_ID, c.TOKEN)
    result = party.join(c.TARGET_PARTY)
    assert isinstance(result, error.NotFoundError)
    assert result.message == "Not found."
