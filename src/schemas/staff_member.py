from schemas.base import BaseSchema
from odmantic.bson import ObjectId


class StaffMember(BaseSchema):
    id: ObjectId
    name: str
    email: str
    mobile: str
    image: str
