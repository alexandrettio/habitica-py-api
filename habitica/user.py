from habitica import error
from habitica.common import HabiticaEndpointsProcessor
from models.common_model import Response


class UserClient(HabiticaEndpointsProcessor):
    @staticmethod
    def _map_error(data, schema) -> Response:
        if data["success"] is False:
            e = getattr(error, f"{data['error']}Error")
            raise e(data["message"])
        return schema.parse_obj(data)

    def allocate_point(self, stat):
        pass

    def allocate_all(self):
        pass

    def allocate_bulk(self, stats):
        pass

    def block_user(self, user_id):
        pass

    def buy_health_potion(self):
        pass

    def buy_mystery_set(self, item_key):
        pass

    def buy_gear(self, item_key):
        pass

    def buy_quest(self, item_key):
        pass

    def buy_armoire(self):
        pass

    def buy(self, item_key):
        pass

    def buy_special_spell(self, item_key):
        pass
