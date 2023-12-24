from datetime import datetime
from odmantic.bson import ObjectId

from schemas.base import BaseSchema
from pydantic import Field


class NewVisitorDrinks(BaseSchema):
    drink_id: ObjectId = Field(alias="drinkId")


class VisitorDrinks(BaseSchema):
    id: ObjectId
    visitor_id: ObjectId = Field(alias="visitorId")
    drink_id: ObjectId = Field(alias="drinkId")
    serve_time: datetime = Field(default=..., alias="visitingTime")
