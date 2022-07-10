from typing import Optional
from urllib.parse import urljoin
import requests


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

    def get_user_info(self) -> requests.Response:
        url = urljoin(self.base_url, "user")
        return requests.get(url=url, headers=self._get_auth_headers())
