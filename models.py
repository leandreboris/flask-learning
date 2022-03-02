from flask_marshmallow import Schema
from app import db
from marshmallow import fields


class Student(db.Document):
    name = db.StringField(required=True)
    field = db.StringField(required=True)

class StudentSchema(Schema):
    id = fields.String()
    name = fields.String(required=True)
    field = fields.String(required=True)