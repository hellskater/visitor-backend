from fastapi import APIRouter, Depends

from models.staff_member import StaffMemberModel
from schemas.staff_member import StaffMember
from settings import Engine
from utils.security import get_user_instance

router = APIRouter()


@router.get(
    path="/staff",
    response_model=list[StaffMember],
    dependencies=[Depends(dependency=get_user_instance)],
)
async def get_staff_members() -> list[StaffMember]:
    staff_members = await Engine.find(model=StaffMemberModel)
    return [StaffMember(**staff_member.model_dump()) for staff_member in staff_members]
