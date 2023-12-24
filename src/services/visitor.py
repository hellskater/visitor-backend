from fastapi import HTTPException
from odmantic import AIOEngine, ObjectId

from models.visitor import VisitorModel
from schemas.visitor import Visitor


async def create_new_visitor(engine: AIOEngine, visitor: VisitorModel) -> Visitor:
    new_visitor = await engine.save(instance=visitor)
    return Visitor(**new_visitor.model_dump())


async def fetch_visitor_by_id(engine: AIOEngine, visitor_id: ObjectId) -> Visitor:
    visitor = await engine.find_one(VisitorModel, VisitorModel.id == visitor_id)
    if not visitor:
        raise HTTPException(status_code=404, detail="Visitor not found")
    return Visitor(**visitor.model_dump())
