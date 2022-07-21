from pydantic import BaseModel, Field
from pydantic.types import Dict, List


def to_lower_camel_case(string: str) -> str:
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


class HabiticaBaseModel(BaseModel):
    class Config:
        alias_generator = to_lower_camel_case


class Response(HabiticaBaseModel):
    from models.notification_model import Notification

    success: bool
    app_version: str
    notifications: List[Notification] = Field(default_factory=list)


class EmptyResponse(Response):
    data: Dict
