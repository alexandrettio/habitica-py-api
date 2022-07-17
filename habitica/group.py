import json
from types import SimpleNamespace
from typing import Optional

import requests

from consts import GroupType, Keep, KeepChallenges, Privacy
from habitica import error
from habitica.common import HabiticaEndpointsProcessor
from models.group_model import (
    AddManagerResponse,
    GetGroupInfoResponse,
    GetGroupsResponse,
    GroupCreateResponse,
    GroupJoinResponse,
    InviteResponse,
    NoDataResponse,
    RemoveManagerResponse,
)


class GroupClient(HabiticaEndpointsProcessor):
    @staticmethod
    def _map_error(data, schema):
        x = json.loads(data.text, object_hook=lambda d: SimpleNamespace(**d))
        if x.success is False:
            e = getattr(error, f"{x.error}Error")
            return e(x.message)
        return schema.parse_obj(data.json())

    def _invite(self, data: dict, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/invite")
        response = requests.post(url=url, json=data, headers=self._get_auth_headers())
        return self._map_error(response, InviteResponse)

    def invite_by_uuid(self, user_id: str, group_id: str = "party"):
        data = {"uuids": [user_id]}
        return self._invite(data, group_id)

    def invite_by_email(self, email: str, name: str = "", group_id: str = "party"):
        data = {"emails": {"email": email, "name": name}}
        return self._invite(data, group_id)

    def reject_invite(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/reject-invite")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response, NoDataResponse)

    def join(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/join")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response, GroupJoinResponse)

    def leave(
        self,
        group_id: str = "party",
        keep: Optional[Keep] = None,
        keep_challenges: Optional[KeepChallenges] = None,
    ):
        url = self._build_url(f"groups/{group_id}/leave")
        params, data = {}, {}
        if keep is not None and keep in list(Keep):
            params = {"keep": keep}
        if keep_challenges is not None and keep_challenges in list(KeepChallenges):
            data = {"keepChallenges": keep_challenges}
        response = requests.post(
            url=url, headers=self._get_auth_headers(), params=params, json=data
        )
        return self._map_error(response, NoDataResponse)

    def remove_member(self, user_id: str, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/removeMember/{user_id}")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response, NoDataResponse)

    def get_info(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}")
        response = requests.get(url, headers=self._get_auth_headers())
        return self._map_error(response, GetGroupInfoResponse)

    def get_groups(self, group_types: str, paginate: bool = None, page: int = None):
        url = self._build_url("groups")
        params = {"type": group_types}
        if paginate is not None:
            params["paginate"] = paginate
        if page is not None:
            params["page"] = page
        response = requests.get(url, headers=self._get_auth_headers(), params=params)
        return self._map_error(response, GetGroupsResponse)

    def create(self, name: str, group_type: GroupType, privacy: GroupType):
        if group_type not in list(GroupType):
            return error.BadRequestError("Incorrect group type.")
        if privacy not in list(Privacy):
            return error.BadRequestError("Incorrect privacy type.")

        url = self._build_url("groups")
        data = {
            "name": name,
            "type": group_type.value,
            "privacy": privacy.value,
        }
        response = requests.post(url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response, GroupCreateResponse)

    def update(self, data: dict, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}")
        response = requests.put(url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response, GroupCreateResponse)

    def add_manager(self, user_id: str, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/add-manager")
        data = {"managerId": user_id}
        response = requests.post(url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response, AddManagerResponse)

    def remove_manager(self, user_id: str, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/remove-manager")
        data = {"managerId": user_id}
        response = requests.post(url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response, RemoveManagerResponse)
