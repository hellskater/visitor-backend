from fastapi import APIRouter, status
from models.visitor import VisitorModel

from schemas.visitor import NewVisitor, Visitor
from services.visitor import create_new_visitor
from settings import Engine


router = APIRouter()


@router.post(
    path="/visitor", response_model=Visitor, status_code=status.HTTP_201_CREATED
)
async def add_new_visitor(visitor: NewVisitor) -> Visitor:
    visitor_instance = VisitorModel(**visitor.model_dump())
    new_visitor = await create_new_visitor(engine=Engine, visitor=visitor_instance)
    return new_visitor
