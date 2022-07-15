from pydantic import BaseModel, Field, UUID4
from pydantic.types import List, Dict


class Response(BaseModel):
    success: bool
    appVersion: str


class NotificationData(BaseModel):
    header_text: str = Field(alias="headerText")
    body_text: str = Field(alias="bodyText")


class Notification(BaseModel):
    notification_type: str = Field(alias="type")  # TODO: enum
    data: NotificationData
    seen: bool
    id: str


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
    get_gems: bool = Field(alias="getGems")


class TasksOrder(BaseModel):
    pass
    # "tasksOrder": {
    #             "habits": [
    #
    #             ],
    #             "dailys": [
    #
    #             ],
    #             "todos": [
    #
    #             ],
    #             "rewards": [
    #
    #             ]
    #         },


class Purchased(BaseModel):
    pass
    # "purchased": {
    #             "plan": {
    #                 "consecutive": {
    #                     "count": 0,
    #                     "offset": 0,
    #                     "gemCapExtra": 0,
    #                     "trinkets": 0
    #                 },
    #                 "quantity": 1,
    #                 "extraMonths": 0,
    #                 "gemsBought": 0,
    #                 "mysteryItems": [
    #
    #                 ]
    #             }
    #         },


class Leader(BaseModel):
    pass
    # {
    #    "auth": {
    #       "local": {
    #          "username": "second_test_api"
    #       }
    #    },
    #    "flags": {
    #       "verifiedUsername": true
    #    },
    #    "profile": {
    #       "name": "second_test_api"
    #    },
    #    "_id": "f4475b35-9f02-4371-9cd8-5fe54c00a9de",
    #    "id": "f4475b35-9f02-4371-9cd8-5fe54c00a9de"
    # },


class GroupBaseInfo(BaseModel):
    id: UUID4
    secret_id: UUID4 = Field(alias="_id")
    summary: str
    privacy: str  # TODO: enum "private"
    member_count: int = Field(alias="memberCount")
    balance: int
    group_type: str = Field(alias="type")  # TODO enum
    name: str
    categories: List
    leader: UUID4 = Field(alias="leader")


class GroupFullInfo(GroupBaseInfo):
    leader_only: LeaderOnly = Field(alias="leaderOnly")
    quest: Quest
    challenge_count: int = Field(alias="challengeCount")
    tasks_order: TasksOrder = Field(alias="tasksOrder")
    purchased: Purchased
    chat: List
    managers: Dict
    leader: Leader


class GetGroupInfoResponse(Response):
    data: GroupFullInfo
    notifications: List[Notification]


class GetGroupsResponse(Response):
    data: List[GroupBaseInfo]
    notifications: List[Notification]
