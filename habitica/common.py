from urllib.parse import urljoin

from pydantic import Field
from pydantic.types import Dict, List

from models.common_model import HabiticaBaseModel


class HabiticaEndpointsProcessor:
    base_url = "https://habitica.com/api/v3/"

    def _get_auth_headers(self) -> dict:
        return {
            "x-api-user": self.user_id,
            "x-api-key": self.token,
            "x-client": f"{self.user_id}-python-api",
        }

    def _build_url(self, relative_url):
        return urljoin(self.base_url, relative_url)

    def __init__(self, user_id: str, token: str) -> None:
        self.user_id = user_id
        self.token = token


class Response(HabiticaBaseModel):
    from models.notification_model import Notification

    success: bool
    app_version: str
    notifications: List[Notification] = Field(default_factory=list)


class EmptyResponse(Response):
    data: Dict
