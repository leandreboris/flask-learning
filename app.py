from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models import *

# App configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask'
# 'sqlite:////tmp/<db_name>.db'

db = SQLAlchemy(app)
marshmallow = Marshmallow(app)


# Controller
@app.route('/students/', methods =['GET'])
def find_all_students():
    get_students = Student.query.all()
    student_schema = StudentSchema(many=True)
    students = student_schema.dump(get_students)
    return make_response(jsonify({"students": students}), 200)


@app.route('/students/', methods=['POST'])
def create_student():
    data = request.get_json()
    student_schema = StudentSchema()
    student = student_schema.load(data, session=db.session)  
    student = Student(name=student.name, field=student.field)
    db.session.add(student)
    db.session.commit()
    result = student_schema.dump(student)  
    return make_response(jsonify({"student": result}),200)


if __name__ == '__main__':
    app.run(debug=True)

