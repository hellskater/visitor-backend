from fastapi import APIRouter, Depends, status
from odmantic import ObjectId
from models.visitor import VisitorModel

from schemas.visitor import NewVisitor, NewVisitorResponse, Visitor
from services.visitor import fetch_visitor_by_id, create_new_visitor
from settings import Engine
from utils.security import create_access_token, is_valid_token


router = APIRouter()


@router.post(
    path="/visitor", response_model=NewVisitorResponse, status_code=status.HTTP_201_CREATED
)
async def add_new_visitor(visitor: NewVisitor) -> NewVisitorResponse:
    visitor_instance = VisitorModel(**visitor.model_dump())
    new_visitor = await create_new_visitor(engine=Engine, visitor=visitor_instance)
    token = create_access_token(user=new_visitor)
    response = NewVisitorResponse(user=new_visitor, token=token)
    return response


@router.get(
    path="/visitor/{visitor_id}",
    response_model=Visitor,
    dependencies=[Depends(is_valid_token)],
)
async def get_visitor_by_id(visitor_id: ObjectId) -> Visitor:
    visitor = await fetch_visitor_by_id(engine=Engine, visitor_id=visitor_id)
    return visitor
