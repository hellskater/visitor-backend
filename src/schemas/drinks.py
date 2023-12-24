from odmantic.bson import ObjectId
from pydantic import Field

from schemas.base import BaseSchema
from schemas.staff_member import StaffMember


class Drink(BaseSchema):
    id: ObjectId
    name: str
    image: str
    staff_member_id: StaffMember = Field(alias="staffMember")
