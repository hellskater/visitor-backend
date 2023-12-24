from odmantic import AIOEngine

from models.visitor import VisitorModel
from schemas.visitor import Visitor


async def create_new_visitor(engine: AIOEngine, visitor: VisitorModel) -> Visitor:
    new_visitor = await engine.save(instance=visitor)
    return Visitor(**new_visitor.model_dump())
