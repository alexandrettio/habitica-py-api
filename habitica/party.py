from urllib.parse import urljoin

import requests

from habitica import error
from habitica.client import Client


class Party(Client):
    def join(self, group_id):
        url = urljoin(self.base_url, f"groups/{group_id}/join")
        response = requests.get(url=url, headers=self._get_auth_headers())
        json = response.json()
        if json["success"] is False:
            e = getattr(error, f"{json['error']}Error")
            return e(json["message"])
