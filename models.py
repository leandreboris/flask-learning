from app import db
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

# Models and Schemas
class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    field = db.Column( db.String(128))


    def __init__(self,name, field) :
        self.name = name
        self.field = field
    

    def __repr__(self) -> str:
        return super().__repr__()

db.create_all()

class StudentSchema(SQLAlchemySchema):
    class Meta:
        model = Student
        load_instance = True
    id = auto_field()
    name =  auto_field()
    field = auto_field()