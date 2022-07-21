from pydantic import BaseModel


def to_lower_camel_case(string: str) -> str:
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


class HabiticaBaseModel(BaseModel):
    class Config:
        alias_generator = to_lower_camel_case
