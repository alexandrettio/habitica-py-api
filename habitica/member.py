from habitica import error
from habitica.common import HabiticaEndpointsProcessor
from models.common_model import Response


class MemberClient(HabiticaEndpointsProcessor):
    @staticmethod
    def _map_error(data, schema) -> Response:
        if data["success"] is False:
            e = getattr(error, f"{data['error']}Error")
            raise e(data["message"])
        return schema.parse_obj(data)

    def get_challenge_member_progress(self, challenge_id: str, member_id: str):
        pass

    def get_member_profile(self, member_id: str):
        pass

    def get_member_achievements(self, member_id: str):
        pass

    def get_challenge_members(self, challenge_id: str):
        pass

    def send_gem_gift(self, message: str, to_user: str, amount: int):
        pass

    def send_private_message(self, message: str, to_user: str):
        pass
