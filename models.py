from app import db, marshmallow
from marshmallow import fields

# Models and Schemas
class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    field = db.Column( db.String(128))

    def __init__(self, name, field) :
        self.name = name
        self.field = field

    def __repr__(self) -> str:
        return super().__repr__()

db.create_all()

class StudentSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Student
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name =  fields.String(required=True)
    field = fields.String(required=True)