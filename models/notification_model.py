from pydantic import BaseModel, Field

from consts import NotificationType
from models.utils import to_lower_camel_case


class NotificationData(BaseModel):
    header_text: str
    body_text: str

    class Config:
        alias_generator = to_lower_camel_case


class Notification(BaseModel):
    notification_type: NotificationType = Field(alias="type")
    data: NotificationData
    seen: bool
    id: str
