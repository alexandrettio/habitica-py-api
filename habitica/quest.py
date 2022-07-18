import requests

from habitica import error
from habitica.common import HabiticaEndpointsProcessor
from models.group_model import Response
from models.quest_model import CancelQuestResponse, QuestInviteResponse


class QuestClient(HabiticaEndpointsProcessor):
    @staticmethod
    def _map_error(data, schema) -> Response:
        if data["success"] is False:
            e = getattr(error, f"{data['error']}Error")
            raise e(data["message"])
        return schema.parse_obj(data)

    def abort(self, group_id: str = "party"):
        pass

    def accept(self, group_id: str = "party"):
        pass

    def cancel(self, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/quests/cancel")
        response = requests.post(url, headers=self._get_auth_headers())
        return self._map_error(response.json(), CancelQuestResponse)

    def force_start(self, group_id: str = "party"):
        pass

    def invite(self, quest_key: str, group_id: str = "party"):
        url = self._build_url(f"groups/{group_id}/quests/invite/{quest_key}")
        response = requests.post(url, headers=self._get_auth_headers())
        return self._map_error(response.json(), QuestInviteResponse)

    def leave(self, group_id: str = "party"):
        pass

    def reject(self, group_id: str = "party"):
        pass
