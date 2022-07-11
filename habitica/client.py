from urllib.parse import urljoin
import requests

from habitica.common import HabiticaEndpointsProcessor
from habitica.group import GroupClient


class HabiticaStats:
    def __init__(self, stats):
        pass


class HabiticaInvites:
    def __init__(self, invitations):
        pass


class HabiticaUser:
    def __init__(self, data: dict):
        self.id = data.get("id", "")
        self.username = data.get("auth", {}).get("local", {}).get("username", "")
        self.profile_name = data.get("profile", {}).get("name", "")
        self.party = data.get("party", {}).get("_id", "")
        self.stats = HabiticaStats(data.get("stats"))
        self.invites = HabiticaInvites(data.get("invitations"))


class Client(HabiticaEndpointsProcessor):
    def __init__(self, user_id: str, token: str) -> None:
        super(Client, self).__init__(user_id, token)
        self.group = GroupClient(user_id, token)

    def get_user_info(self) -> HabiticaUser:
        url = self.build_url("user")
        response = requests.get(url=url, headers=self._get_auth_headers())
        json = response.json()
        if response.ok and json.get("success"):
            return HabiticaUser(json.get("data"))
