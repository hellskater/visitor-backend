from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status

from models.staff_member import StaffMemberModel
from models.visitor import VisitorModel
from models.visitor_details import VisitingDetailsModel
from schemas.visiting_details import NewVisitingDetails, VisitingDetails
from schemas.visitor import Visitor
from services.visiting_details import create_new_visiting_details
from settings import Engine
from utils.security import get_user_instance
from utils.sms import send_sms

router = APIRouter()


@router.post(
    path="/visiting",
    response_model=VisitingDetails,
    status_code=status.HTTP_201_CREATED,
)
async def add_new_visiting_details(
    visiting_details: NewVisitingDetails,
    user: Annotated[Visitor, Depends(dependency=get_user_instance)],
    background_tasks: BackgroundTasks,
) -> VisitingDetails:
    staff_member = await Engine.find_one(
        StaffMemberModel, StaffMemberModel.id == visiting_details.staff_member_id
    )
    visitor = await Engine.find_one(VisitorModel, VisitorModel.id == user.id)

    if not staff_member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff member not found",
        )

    if not visitor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Visitor not found",
        )

    visiting_details_dict = visiting_details.model_dump()
    visiting_details_dict["staff_member_id"] = staff_member

    visiting_details_instance = VisitingDetailsModel(
        **visiting_details_dict,
        visitor_id=visitor,
    )
    new_visiting_details = await create_new_visiting_details(
        engine=Engine, visiting_details=visiting_details_instance
    )

    if visiting_details.send_notification:
        background_tasks.add_task(
            send_sms,
            phone_number=staff_member.mobile,
            message=f"Hello {staff_member.name}, you have"
            f" an appointment with {visitor.name} for {visiting_details.reason}",
        )

    return new_visiting_details
