from typing import Optional

from pydantic import UUID4, BaseModel, Field
from pydantic.types import Dict

from models.group_model import Response


class ProgressInfo(BaseModel):
    collect: Dict
    hp: Optional[float]


class QuestInfo(BaseModel):
    progress: ProgressInfo
    active: bool
    members: Dict
    extra: Optional[Dict]
    key: Optional[str] = ""
    quest_leader: UUID4 = Field(default=None, alias="leader")


class QuestResponse(Response):
    data: QuestInfo
