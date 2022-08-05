from typing import Dict

from pydantic import UUID4, Field

from models.common_model import HabiticaBaseModel, Response
from models.user_model import Items, Preferences, Stats


class UserStyle(HabiticaBaseModel):
    items: Items = Field(default=None)
    preferences: Preferences = Field(default=None)
    stats: Stats = Field(default=None)


class Message(HabiticaBaseModel):
    flag_count: int = Field(default=None)
    flags: Dict = Field(default=None)  # TODO: Flag schema
    secret_id: UUID4 = Field(alias="_id")
    id: UUID4
    text: str
    unformatted_text: str
    info: Dict = Field(default=None)  # TODO Info schema
    timestamp: str  # TODO past date
    likes: Dict = Field(default=None)  # TODO Likes schema
    client: str = Field(default=None)
    uuid: UUID4
    contributor: Dict = Field(default=None)
    backer: Dict = Field(default=None)
    user: str
    username: str
    group_id: UUID4
    user_styles: UserStyle


class MessageData(HabiticaBaseModel):
    message: Message


class CreateMessageResponse(Response):
    data: MessageData
