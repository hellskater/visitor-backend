from typing import Annotated
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status

from models.drinks import DrinkModel
from models.visitor import VisitorModel
from models.visitor_drinks import VisitorDrinksModel
from schemas.drinks import Drink
from schemas.visitior_drinks import NewVisitorDrinks, VisitorDrinks
from schemas.visitor import Visitor
from services.visitor_drinks import create_new_visitor_drink
from settings import Engine
from models.staff_member import StaffMemberModel
from utils.sms import send_sms
from utils.security import get_user_instance

router = APIRouter()


@router.get(
    path="/drinks",
    response_model=list[Drink],
    dependencies=[Depends(dependency=get_user_instance)],
)
async def get_drinks() -> list[Drink]:
    drinks = await Engine.find(model=DrinkModel)
    return [Drink(**drink.model_dump()) for drink in drinks]


@router.post(
    path="/drinks/visitor",
    response_model=VisitorDrinks,
    status_code=status.HTTP_201_CREATED,
)
async def add_new_visitor_drink(
    visitor_drink: NewVisitorDrinks,
    user: Annotated[Visitor, Depends(dependency=get_user_instance)],
    background_tasks: BackgroundTasks,
) -> VisitorDrinks:
    drink = await Engine.find_one(DrinkModel, DrinkModel.id == visitor_drink.drink_id)
    visitor = await Engine.find_one(VisitorModel, VisitorModel.id == user.id)

    if not drink:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Drink not found",
        )

    if not visitor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Visitor not found",
        )

    staff_member_id = str(drink.staff_member_id)

    staff_member = await Engine.find_one(
        StaffMemberModel, StaffMemberModel.id == staff_member_id
    )

    visitor_drink_dict = visitor_drink.model_dump()
    visitor_drink_dict["drink_id"] = drink

    visitor_drink_instance = VisitorDrinksModel(
        **visitor_drink_dict,
        visitor_id=visitor,
    )
    new_visitor_drink = await create_new_visitor_drink(
        engine=Engine, visitor_drink=visitor_drink_instance
    )

    if staff_member:
        background_tasks.add_task(
            send_sms,
            phone_number=staff_member.mobile,
            message=f"Hello {staff_member.name}, you have"
            f" a new drink request from {visitor.name}",
        )

    return new_visitor_drink
