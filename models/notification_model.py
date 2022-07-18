from pydantic import UUID4, BaseModel, Field

from consts import NotificationType
from models.utils import to_lower_camel_case


class GroupNotification(BaseModel):
    id: UUID4
    name: str


class NotificationData(BaseModel):
    header_text: str = Field(default=None)
    body_text: str = Field(default=None)
    group: GroupNotification = Field(default=None)

    class Config:
        alias_generator = to_lower_camel_case


class Notification(BaseModel):
    notification_type: NotificationType = Field(alias="type")
    data: NotificationData
    seen: bool
    id: str
