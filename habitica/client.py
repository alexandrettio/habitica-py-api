from urllib.parse import urljoin
import requests


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


class Client:
    base_url = "https://habitica.com/api/v3/"

    def __init__(self, user_id: str, token: str) -> None:
        self.user_id = user_id
        self.token = token

    def _get_auth_headers(self) -> dict:
        return {
            "x-api-user": self.user_id,
            "x-api-key": self.token
        }

    def get_user_info(self) -> HabiticaUser:
        url = urljoin(self.base_url, "user")
        response = requests.get(url=url, headers=self._get_auth_headers())
        json = response.json()
        if response.ok and json.get("success"):
            return HabiticaUser(json.get("data"))

