from datetime import datetime

from odmantic import Field, Model, Reference

from models.drinks import DrinkModel
from models.visitor import VisitorModel


class VisitorDrinksModel(Model):
    drink_id: DrinkModel = Reference()
    visitor_id: VisitorModel = Reference()
    serve_time: datetime = Field(default_factory=datetime.utcnow)
