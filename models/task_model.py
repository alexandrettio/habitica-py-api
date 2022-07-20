from pydantic import UUID4, BaseModel, Field
from pydantic.datetime_parse import datetime
from pydantic.types import Dict, List

from consts import AttributeType, TaskType
from models.group_model import Response
from models.utils import to_lower_camel_case


class TaskHistory(BaseModel):
    value: float
    date: str  # TODO check format


class Task(BaseModel):
    id: UUID4
    secret_id: UUID4 = Field(alias="_id")
    user_id: UUID4
    text: str
    alias: str = Field(default=None)
    type: TaskType
    notes: str
    tags: List  # TODO: List of tags
    value: float
    priority: float  # TODO think about enum
    attribute: AttributeType
    reminders: List  # TODO List of reminders
    created_at: datetime = Field(default=None)
    updated_at: datetime = Field(default=None)
    down: bool = Field(default=None)
    up: bool = Field(default=None)
    challenge: Dict  # TODO Challenge class
    group: Dict  # TODO no ideas what it means yet
    history: List[TaskHistory] = Field(default=None)

    class Config:
        alias_generator = to_lower_camel_case


class TaskResponse(Response):
    data: Task
