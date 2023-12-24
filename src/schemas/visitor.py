from datetime import datetime

from pydantic import Field

from schemas.base import BaseSchema


class NewVisitor(BaseSchema):
    name: str
    mobile: str
    address: str


class Visitor(BaseSchema):
    name: str
    mobile: str
    address: str
    sign_in_time: datetime = Field(..., alias="signInTime")
