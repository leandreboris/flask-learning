from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from models import *

# App configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask'
# 'sqlite:////tmp/<db_name>.db'

db = SQLAlchemy(app)


# Controller
@app.route('/students/', methods =['GET'])
def find_all_students():
    get_students = Student.query.all()
    student_schema = StudentSchema(many=True)
    students = student_schema.dump(get_students)
    return make_response(jsonify({"students": students}), 200)

@app.route('/students/<id>/', methods=['GET'])
def find_student_by_id(id):
    student_schema = StudentSchema()
    student = Student.query.get(id)
    student = student_schema.dump(student)
    return make_response(jsonify({'student' : student}), 200)

@app.route('/students/<id>/', methods = ['DELETE'])
def delete_student_by_id(id):
    student = Student.query.get(id)
    print(student)
    student.delete()
    return make_response("OK",204)

@app.route('/students/<id>/', methods = ['PUT'])
def update_student_by_id(id):
    data = request.get_json()
    student = Student.query.get(id)
    if data.get('name'):
        student.name = data['name']
    if data.get('field'):
        student.field = data['field']
    student.save()
    student_schema = StudentSchema(only=['id', 'name','field'])
    student = student_schema.dump(student)
    return make_response(jsonify({"student": student}))

@app.route('/students/', methods=['POST'])
def create_student():
    data = request.get_json()
    student_schema = StudentSchema()
    student = student_schema.load(data, session=db.session) 
    student = Student(name=student.name, field=student.field)
    student.save()
    result = student_schema.dump(student)  
    return make_response(jsonify({"student": result}),200)



if __name__ == '__main__':
    app.run(debug=True)

