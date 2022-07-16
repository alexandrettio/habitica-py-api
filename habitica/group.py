import json
from types import SimpleNamespace
from typing import Optional

import requests

from consts import PARTY, GUILDS, REMOVE_ALL, KEEP_ALL, REMAIN_IN_CHALLENGES, LEAVE_CHALLENGES, PrivacyEnum, \
    GroupTypeEnum
from habitica import error
from habitica.common import HabiticaEndpointsProcessor
from models.group_model import GetGroupInfoResponse, GetGroupsResponse, AddManagerResponse


class GroupClient(HabiticaEndpointsProcessor):
    @staticmethod
    def _map_error(data, schema=None):
        x = json.loads(data.text, object_hook=lambda d: SimpleNamespace(**d))
        if x.success is False:
            e = getattr(error, f"{x.error}Error")
            return e(x.message)
        if schema is not None:
            return schema.parse_obj(data.json())
        return data

    def _invite(self, data: dict, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/invite")
        response = requests.post(url=url, json=data, headers=self._get_auth_headers())
        return self._map_error(response)

    def invite_by_uuid(self, user_id: str, group_id: str = "party"):
        data = {"uuids": [user_id]}
        return self._invite(data, group_id)

    def invite_by_email(self, email: str, name: str = "", group_id: str = "party"):
        data = {"emails": {"email": email, "name": name}}
        return self._invite(data, group_id)

    def reject_invite(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/reject-invite")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response)

    def join(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/join")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response)

    def leave(self, group_id: str = "party", keep: Optional[str] = None, keep_challenges: Optional[str] = None):
        url = self._build_url(f"groups/{group_id}/leave")
        params, data = {}, {}
        if keep is not None and keep in (REMOVE_ALL, KEEP_ALL):
            params = {"keep": keep}
        if keep_challenges is not None and keep_challenges in (REMAIN_IN_CHALLENGES, LEAVE_CHALLENGES):
            data = {"keepChallenges": keep_challenges}
        response = requests.post(url=url, headers=self._get_auth_headers(), params=params, json=data)
        return self._map_error(response)

    def remove_member(self, user_id: str, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/removeMember/{user_id}")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response)

    def get_info(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}")
        response = requests.get(url, headers=self._get_auth_headers())
        return self._map_error(response, GetGroupInfoResponse)

    def get_groups(self, group_types: str, paginate: bool = None, page: int = None):
        url = self._build_url(f"groups")
        params = {"type": group_types}
        if paginate is not None:
            params["paginate"] = paginate
        if page is not None:
            params["page"] = page
        response = requests.get(url, headers=self._get_auth_headers(), params=params)
        return self._map_error(response, GetGroupsResponse)

    def create(self, name: str, group_type: str, privacy: str):
        if group_type not in list(GroupTypeEnum):
            return error.BadRequestError("Incorrect group type.")
        if privacy not in list(PrivacyEnum):
            return error.BadRequestError("Incorrect privacy type.")

        url = self._build_url("groups")
        data = {
            "name": name,
            "type": group_type,
            "privacy": privacy,
        }
        response = requests.post(url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response)

    def update(self, data: dict, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}")
        response = requests.put(url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response)

    def add_manager(self, user_id: str, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/add-manager")
        data = {"managerId": user_id}
        response = requests.post(url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response, AddManagerResponse)

    def remove_manager(self, user_id: str, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/remove-manager")
        data = {"managerId": user_id}
        response = requests.post(url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response)
