from pydantic import UUID4, BaseModel, Field
from pydantic.types import Dict, List

from consts import GroupTypeEnum, PrivacyEnum
from models.notification_model import Notification
from models.utils import to_lower_camel_case


class Response(BaseModel):
    success: bool
    app_version: str
    notifications: List[Notification] = Field(default_factory=list)

    class Config:
        alias_generator = to_lower_camel_case


class QuestProgress(BaseModel):
    collect: Dict


class Member(BaseModel):
    pass


class Quest(BaseModel):
    progress: QuestProgress
    active: bool
    members: Member
    extra: Dict


class LeaderOnly(BaseModel):
    challenges: bool
    get_gems: bool

    class Config:
        alias_generator = to_lower_camel_case


class TasksOrder(BaseModel):
    habits: List
    dailys: List
    todos: List
    rewards: List


class Plan(BaseModel):
    consecutive: Dict
    #                 "consecutive": {
    #                     "count": 0,
    #                     "offset": 0,
    #                     "gemCapExtra": 0,
    #                     "trinkets": 0
    #                 },
    quantity: int
    extra_months: int
    gems_bought: int
    mystery_items: List

    class Config:
        alias_generator = to_lower_camel_case


class Purchased(BaseModel):
    plan: Plan = Field(default=None)


class Leader(BaseModel):
    id: UUID4 = Field(default=None)
    secret_id: UUID4 = Field(alias="_id")
    auth: Dict = Field(default=None)
    # {
    #    "auth": {
    #       "local": {
    #          "username": "second_test_api"
    #       }
    #    },
    flags: Dict = Field(default=None)
    #    "flags": {
    #       "verifiedUsername": true
    #    },
    profile: Dict = Field(default=None)
    #    "profile": {
    #       "name": "second_test_api"
    #    },
    # },


class GroupBaseInfo(BaseModel):
    id: UUID4
    secret_id: UUID4 = Field(alias="_id")
    summary: str = Field(default=None)
    privacy: PrivacyEnum
    member_count: int = Field(default=0, gt=-1)
    balance: int = Field(default=None, gt=-1)
    group_type: GroupTypeEnum = Field(alias="type")
    name: str
    categories: List
    leader: UUID4
    managers: Dict = Field(default=None)


class GroupFullInfo(GroupBaseInfo):
    leader_only: LeaderOnly
    quest: Quest
    challenge_count: int
    tasks_order: TasksOrder
    purchased: Purchased
    chat: List
    leader: Leader

    class Config:
        alias_generator = to_lower_camel_case


class GetGroupInfoResponse(Response):
    data: GroupFullInfo


class GetGroupsResponse(Response):
    data: List[GroupBaseInfo]


class AddManagerResponse(Response):
    data: GroupBaseInfo


class GroupCreateResponse(Response):
    data: GroupFullInfo


class NoDataResponse(Response):
    data: Dict = Field(default=None)


class RemoveManagerResponse(Response):
    data: GroupBaseInfo
