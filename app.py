from flask import Flask, request, jsonify, make_response
from flask_mongoengine import MongoEngine
from marshmallow import Schema, fields, post_load
from bson import ObjectId
from models import *



app = Flask(__name__)
app.config['MONGODB_DB'] = 'students'
db = MongoEngine(app)
Schema.TYPE_MAPPING[ObjectId] = fields.String


@app.route('/students/', methods = ['GET'])
def get_all_students():
    students = Student.objects.all()
    student_schema =StudentSchema(many=True)
    students = student_schema.dump(students)
    return make_response(jsonify({"students": students}), 200)


@app.route('/students/<id>/', methods=['GET'])
def find_student_by_id(id):
    student = Student.objects.get_or_404(id=ObjectId(id))
    student_schema = StudentSchema()
    student = student_schema.dump(student)
    return make_response(jsonify({'student' : student}), 200)

@app.route('/students/', methods = ['POST'])
def create_student():
    data = request.get_json()
    student = Student(name=data['name'],field=data['field'])
    student.save()
    student_schema = StudentSchema()
    student = student_schema.dump(student)
    return make_response(jsonify({"student": student}),201)

@app.route('/students/<id>/', methods = ['PUT'])
def update_student_by_id(id):
    data = request.get_json()
    student = Student.objects.get_or_404(id=ObjectId(id))
    if data.get('field'):
        student.field = data['field']
    if data.get('name'):
        student.name = data['name']
    student.save()
    student.reload()
    student_schema = StudentSchema()
    student = student_schema.dump(student)
    return make_response(jsonify({"student": student}))

@app.route('/students/<id>/', methods=['DELETE'])
def delete_student_by_id(id):
    student = Student.objects.get_or_404(id=ObjectId(id))
    student.delete()
    return make_response("OK", 204)

if __name__ == '__main__':
    app.run(debug=True)