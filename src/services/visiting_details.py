from odmantic import AIOEngine

from models.visitor_details import VisitingDetailsModel
from schemas.visiting_details import VisitingDetails


async def create_new_visiting_details(
    engine: AIOEngine, visiting_details: VisitingDetailsModel
) -> VisitingDetails:
    new_visiting_details = await engine.save(instance=visiting_details)
    new_visiting_details_dict = new_visiting_details.model_dump()
    new_visiting_details_dict[
        "staff_member_id"
    ] = new_visiting_details.staff_member_id.id
    new_visiting_details_dict["visitor_id"] = new_visiting_details.visitor_id.id
    return VisitingDetails(**new_visiting_details_dict)
