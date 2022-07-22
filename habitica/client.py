import requests
from pydantic.types import Dict, List

from consts import GUILDS, PARTIES, PARTY
from habitica import error
from habitica.challenge import ChallengeClient
from habitica.common import HabiticaEndpointsProcessor
from habitica.group import GroupClient
from habitica.notification import NotificationClient
from habitica.tag import TagClient
from habitica.task import TaskClient
from models.common_model import EmptyResponse, InboxResponse, Response


class HabiticaInvite:
    def __init__(self, invite_data: dict):
        self.id = invite_data.get("id")
        self.name = invite_data.get("name")
        self.inviter = invite_data.get("inviter")
        self._id = invite_data.get("_id")

    def __str__(self):
        return f"invite to {self.name}"


class HabiticaUser:
    def __init__(self, data: dict):
        self.id = data.get("id", "")
        self.username = data.get("auth", {}).get("local", {}).get("username", "")
        self.profile_name = data.get("profile", {}).get("name", "")
        self.party = data.get("party", {}).get("_id", "")
        self.raw_data = data

    def get_invitations(self) -> Dict[str, List[HabiticaInvite]]:
        invitations = self.raw_data.get("invitations")
        invitation_types = (GUILDS, PARTIES)

        result = {}
        for key in invitation_types:
            result[key] = []
            for invite_info in invitations.get(key, []):
                result[key].append(HabiticaInvite(invite_info))
        result[PARTY] = [
            HabiticaInvite(invitations.get(PARTY, {})),
        ]
        return result


class NotAuthClient:
    def __init__(self):
        self.world_state = None
        self.status = None
        self.content = None
        self.meta = None


class Client(HabiticaEndpointsProcessor):
    def __init__(self, user_id: str, token: str) -> None:
        super(Client, self).__init__(user_id, token)
        self.group = GroupClient(user_id, token)
        self.task = TaskClient(user_id, token)
        self.tag = TagClient(user_id, token)
        self.notification = NotificationClient(user_id, token)
        self.challenge = ChallengeClient(user_id, token)
        self.chat = None
        self.data_export = None
        self.members = None
        self.user = None

    @staticmethod
    def _map_error(data: dict, schema) -> Response:
        if data["success"] is False:
            e = getattr(error, f"{data['error']}Error")
            raise e(data["message"])
        return schema.parse_obj(data)

    def cron(self) -> Response:
        url = self._build_url("cron")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json(), EmptyResponse)

    def get_inbox(self, page: int, conversation: str = None):
        url = self._build_url("inbox/messages")
        params = {page: page}
        if conversation is not None:
            params["conversation"] = conversation
        response = requests.get(
            url=url, headers=self._get_auth_headers(), params=params
        )
        return self._map_error(response.json(), InboxResponse)

    def get_user_info(self) -> HabiticaUser:
        url = self._build_url("user")
        response = requests.get(url=url, headers=self._get_auth_headers())
        json = response.json()
        if response.ok and json.get("success"):
            return HabiticaUser(json.get("data"))
