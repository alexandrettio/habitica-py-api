from typing import Optional

import requests

from consts import PARTY, GUILDS, PRIVATE, PUBLIC
from habitica import error
from habitica.common import HabiticaEndpointsProcessor


class HabiticaGroup:
    pass


class GroupClient(HabiticaEndpointsProcessor):
    @staticmethod
    def _map_error(json):
        if json["success"] is False:
            e = getattr(error, f"{json['error']}Error")
            return e(json["message"])
        return json

    def _invite(self, data: dict, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/invite")
        response = requests.post(url=url, json=data, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def invite_by_uuid(self, user_id: str, group_id: str = "party"):
        data = {"uuids": [user_id]}
        return self._invite(data, group_id)

    def invite_by_email(self, email: str, name: str = "", group_id: str = "party"):
        data = {"emails": {"email": email, "name": name}}
        return self._invite(data, group_id)

    def reject_invite(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/reject-invite")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def join(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/join")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def leave(self, group_id: str = "party", keep: Optional[str] = None, keep_challenges: Optional[str] = None):
        url = self._build_url(f"groups/{group_id}/leave")
        params, data = {}, {}
        if keep is not None and keep in ("remove-all", "keep-all"):
            params = {"keep": keep}
        if keep_challenges is not None and keep_challenges in ("remain-in-challenges", "leave-challenges"):
            data = {"keepChallenges": keep_challenges}
        response = requests.post(url=url, headers=self._get_auth_headers(), params=params, json=data)
        return self._map_error(response.json())

    def remove_member(self, user_id: str, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/removeMember/{user_id}")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def get_info(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}")
        response = requests.get(url, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def get_groups(self, group_type: str, paginate: bool = False, page: int = 0):
        pass

    def create(self, name: str, group_type: str, privacy: str):
        if group_type not in (PARTY, GUILDS):
            return error.BadRequestError("Incorrect group type")
        if privacy not in (PRIVATE, PUBLIC):
            return error.BadRequestError("Incorrect privacy type")

        url = self._build_url("groups")
        data = {
            "name": name,
            "type": group_type,
            "privacy": privacy,
        }
        response = requests.post(url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response.json())

    def update(self, data: HabiticaGroup, group_id: str = "party"):
        pass

    def add_manager(self, user_id: str, group_id: str = "party"):
        pass

    def remove_manager(self, user_id: str, group_id: str = "party"):
        pass
