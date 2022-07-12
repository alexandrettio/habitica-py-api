from typing import List, Dict
import requests

from consts import GUILDS, PARTIES, PARTY
from habitica.common import HabiticaEndpointsProcessor
from habitica.group import GroupClient
from habitica.quest import QuestClient


class HabiticaStats:
    def __init__(self, stats):
        pass


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
        result[PARTY] = [HabiticaInvite(invitations.get(PARTY, {})), ]
        return result

    def get_stats(self) -> HabiticaStats:
        pass


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
        self.quest = QuestClient(user_id, token)
        self.challenge = None
        self.chat = None
        self.cron = None
        self.data_export = None
        self.inbox = None
        self.members = None
        self.news = None
        self.notification = None
        self.tag = None
        self.task = None
        self.user = None

    def get_user_info(self) -> HabiticaUser:
        url = self._build_url("user")
        response = requests.get(url=url, headers=self._get_auth_headers())
        json = response.json()
        if response.ok and json.get("success"):
            return HabiticaUser(json.get("data"))
