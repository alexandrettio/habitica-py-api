from urllib.parse import urljoin

import requests

from habitica import error
from habitica.common import HabiticaEndpointsProcessor


class GroupClient(HabiticaEndpointsProcessor):
    @staticmethod
    def _map_error(json):
        if json["success"] is False:
            e = getattr(error, f"{json['error']}Error")
            return e(json["message"])
        return json

    def join(self, group_id: str):
        url = self.build_url(f"groups/{group_id}/join")
        response = requests.get(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def _invite(self, data: dict, group_id: str = "party"):
        url = self.build_url(f"groups/{group_id}/invite")
        response = requests.post(url=url, json=data, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def invite_by_uuid(self, user_id: str, group_id: str = "party"):
        data = {"uuids": [user_id]}
        return self._invite(data)

    def invite_by_email(self, email: str, name: str = "", group_id: str = "party"):
        data = {"emails": {"email": email, "name": name}}
        return self._invite(data)

    def reject_invite(self, group_id: str = "party"):
        url = self.build_url(f"groups/{group_id}/reject-invite")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def remove_member(self, user_id: str, group_id: str = "party"):
        url = self.build_url(f"groups/{group_id}/removeMember/{user_id}")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json())
