from urllib.parse import urljoin

import requests

from habitica import error
from habitica.client import Client


class Party(Client):
    def build_url(self, relative_url):
        return urljoin(self.base_url, relative_url)

    @staticmethod
    def _map_error(json):
        if json["success"] is False:
            e = getattr(error, f"{json['error']}Error")
            return e(json["message"])
        return json

    def join(self, group_id:str):
        url = self.build_url(f"groups/{group_id}/join")
        response = requests.get(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def invite(self, user_id: str, group_id: str = "party"):
        url = self.build_url(f"groups/{group_id}/invite")
        data = {"uuids": [user_id]}
        response = requests.post(url=url, json=data, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def reject_invite(self, group_id: str = "party"):
        url = self.build_url(f"groups/{group_id}/reject-invite")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json())

    def remove_member(self, user_id: str, group_id: str = "party"):
        url = self.build_url(f"groups/{group_id}/removeMember/{user_id}")
        response = requests.post(url=url, headers=self._get_auth_headers())
        return self._map_error(response.json())
