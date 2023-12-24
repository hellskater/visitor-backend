from datetime import datetime

from odmantic import Field, Model


class VisitorModel(Model):
    name: str
    mobile: str
    address: str
    sign_in_time: datetime = Field(default_factory=datetime.utcnow)
