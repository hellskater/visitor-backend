from odmantic import AIOEngine


from models.visitor_drinks import VisitorDrinksModel
from schemas.visitior_drinks import VisitorDrinks


async def create_new_visitor_drink(
    engine: AIOEngine, visitor_drink: VisitorDrinksModel
) -> VisitorDrinks:
    new_visitor_drink = await engine.save(instance=visitor_drink)
    new_visitor_drink_dict = new_visitor_drink.model_dump()
    new_visitor_drink_dict["drink_id"] = new_visitor_drink.drink_id.id
    new_visitor_drink_dict["visitor_id"] = new_visitor_drink.visitor_id.id
    return VisitorDrinks(**new_visitor_drink_dict)
