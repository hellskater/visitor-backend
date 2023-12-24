from datetime import datetime

from odmantic.bson import ObjectId
from pydantic import Field

from schemas.base import BaseSchema


class NewVisitor(BaseSchema):
    name: str
    mobile: str
    address: str


class Visitor(BaseSchema):
    id: ObjectId
    name: str
    mobile: str
    address: str
    sign_in_time: datetime = Field(default=..., alias="signInTime")


class NewVisitorResponse(BaseSchema):
    user: Visitor
    token: str
