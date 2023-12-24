from fastapi import APIRouter, Depends

from models.drinks import DrinkModel
from schemas.drinks import Drink
from settings import Engine
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
