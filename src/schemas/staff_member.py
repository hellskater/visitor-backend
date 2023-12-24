from odmantic.bson import ObjectId

from schemas.base import BaseSchema


class StaffMember(BaseSchema):
    id: ObjectId
    name: str
    email: str
    mobile: str
    image: str
