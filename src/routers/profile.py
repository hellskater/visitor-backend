from typing import Annotated

from fastapi import APIRouter, Depends

from schemas.visitor import Visitor
from utils.security import get_user_instance

router = APIRouter()


@router.get(
    path="/me",
    response_model=Visitor,
)
async def get_visitor_by_id(
    user: Annotated[Visitor, Depends(dependency=get_user_instance)]
) -> Visitor:
    return user
