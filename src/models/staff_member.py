from odmantic import Model


class StaffMemberModel(Model):
    name: str
    image: str
    email: str
    mobile: str
