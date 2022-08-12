import requests

from habitica import error
from habitica.common import HabiticaEndpointsProcessor
from models.common_model import EmptyResponse, Response


class MemberClient(HabiticaEndpointsProcessor):
    @staticmethod
    def _map_error(data, schema) -> Response:
        if data["success"] is False:
            e = getattr(error, f"{data['error']}Error")
            raise e(data["message"])
        return schema.parse_obj(data)

    def get_challenge_member_progress(self, challenge_id: str, member_id: str):
        url = self._build_url(f"challenges/{challenge_id}/members/{member_id}")
        response = requests.get(url=url, headers=self._get_auth_headers())
        # TODO: Choose schema
        return self._map_error(response.json(), Response)

    def get_member_profile(self, member_id: str):
        url = self._build_url(f"members/{member_id}")
        response = requests.get(url=url, headers=self._get_auth_headers())
        # TODO: Choose schema
        return self._map_error(response.json(), Response)

    def get_member_achievements(self, member_id: str):
        url = self._build_url(f"members/{member_id}/achievements")
        response = requests.get(url=url, headers=self._get_auth_headers())
        # TODO: Choose schema
        return self._map_error(response.json(), Response)

    def get_challenge_members(
        self,
        challenge_id: str,
        last_id: str = None,
        limit: int = 30,
        include_tasks: bool = False,
        include_all_public_fields: bool = False,
    ):
        url = self._build_url(f"challenges/{challenge_id}/members")
        params = {"limit": limit, "includeTasks": include_tasks, "includeAllPublicFields": include_all_public_fields}
        if last_id:
            params["lastId"] = last_id
        response = requests.get(url=url, headers=self._get_auth_headers(), params=params)
        # TODO: Choose schema
        return self._map_error(response.json(), Response)

    def send_gem_gift(self, message: str, to_user: str, amount: int):
        url = self._build_url("members/transfer-gems")
        data = {"message": message, "toUserId": to_user, "gemAmount": amount}
        response = requests.post(url=url, headers=self._get_auth_headers(), json=data)
        return self._map_error(response.json(), EmptyResponse)

    def send_private_message(self, message: str, to_user: str):
        url = self._build_url("members/send-private-message")
        data = {"message": message, "toUserId": to_user}
        response = requests.post(url=url, headers=self._get_auth_headers(), json=data)
        # TODO: Choose schema
        return self._map_error(response.json(), Response)
