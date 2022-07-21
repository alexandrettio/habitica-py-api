from pydantic import UUID4, Field

from consts import NotificationType
from models.common_model import HabiticaBaseModel


class GroupNotification(HabiticaBaseModel):
    id: UUID4
    name: str


class NotificationData(HabiticaBaseModel):
    header_text: str = Field(default=None)
    body_text: str = Field(default=None)
    group: GroupNotification = Field(default=None)


class Notification(HabiticaBaseModel):
    notification_type: NotificationType = Field(alias="type")
    data: NotificationData
    seen: bool
    id: str
