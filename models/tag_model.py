from pydantic import UUID4
from pydantic.types import List

from habitica.common import Response
from models.common_model import HabiticaBaseModel


class Tag(HabiticaBaseModel):
    name: str
    id: UUID4


class TagsListResponse(Response):
    data: List[Tag]


class TagResponse(Response):
    data: Tag
