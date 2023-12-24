from datetime import datetime
from odmantic import Field, Model, Reference

from models.visitor import VisitorModel
from models.staff_member import StaffMemberModel


class VisitingDetailsModel(Model):
    staff_member_id: StaffMemberModel = Reference()
    visitor_id: VisitorModel = Reference()
    reason: str
    visiting_time: datetime = Field(default_factory=datetime.utcnow)
    send_notification: bool = False
