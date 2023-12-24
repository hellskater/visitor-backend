from fastapi import APIRouter, status

from models.visitor import VisitorModel
from schemas.visitor import NewVisitor, NewVisitorResponse
from services.visitor import create_new_visitor
from settings import Engine
from utils.security import create_access_token

router = APIRouter()


@router.post(
    path="/visitor",
    response_model=NewVisitorResponse,
    status_code=status.HTTP_201_CREATED,
)
async def add_new_visitor(visitor: NewVisitor) -> NewVisitorResponse:
    visitor_instance = VisitorModel(**visitor.model_dump())
    new_visitor = await create_new_visitor(engine=Engine, visitor=visitor_instance)
    token = create_access_token(user=new_visitor)
    response = NewVisitorResponse(user=new_visitor, token=token)
    return response
