from habitica.common import HabiticaEndpointsProcessor


class QuestClient(HabiticaEndpointsProcessor):
    def abort(self, group_id: str = "party"):
        pass

    def accept(self, group_id: str = "party"):
        pass

    def cancel(self, group_id: str = "party"):
        pass

    def force_start(self, group_id: str = "party"):
        pass

    def invite(self, group_id: str = "party"):
        pass

    def leave(self, group_id: str = "party"):
        pass

    def reject(self, group_id: str = "party"):
        pass
