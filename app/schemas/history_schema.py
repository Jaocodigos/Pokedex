from app.schemas import schema
from app.models.history import History


class HistorySchema(schema.SQLAlchemySchema):
    class Meta:
        model = History

        name = schema.auto_field()
