from typing import Optional

from pydantic import UUID4, BaseModel, Field
from pydantic.types import Dict

from models.group_model import Member, Response


class ProgressInfo(BaseModel):
    collect: Dict
    hp: Optional[float]


class QuestInfo(BaseModel):
    progress: ProgressInfo
    active: bool
    members: Member
    extra: Optional[Dict]
    key: Optional[str] = ""
    quest_leader: UUID4 = Field(default=None, alias="leader")


class QuestInviteResponse(Response):
    data: QuestInfo


class CancelQuestResponse(Response):
    data: QuestInfo
