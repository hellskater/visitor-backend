from datetime import datetime
from odmantic import Field, Model, Reference

from models.staff_member import StaffMemberModel


class DrinkModel(Model):
    name: str
    image: str
    staff_member_id: StaffMemberModel = Reference()
