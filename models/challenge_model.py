from pydantic.types import List

from models.common_model import HabiticaBaseModel, Response


class Challenge(HabiticaBaseModel):
    pass


class ChallengeResponse(Response):
    data: Challenge


class ChallengesListResponse(Response):
    data: List[Challenge]
