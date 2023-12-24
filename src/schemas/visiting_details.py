from datetime import datetime

from odmantic.bson import ObjectId
from pydantic import Field

from schemas.base import BaseSchema


class NewVisitingDetails(BaseSchema):
    staff_member_id: ObjectId = Field(alias="staffMemberId")
    reason: str
    send_notification: bool = Field(default=False, alias="sendNotification")


class VisitingDetails(NewVisitingDetails):
    id: ObjectId
    visitor_id: ObjectId = Field(alias="visitorId")
    visiting_time: datetime = Field(default=..., alias="visitingTime")
