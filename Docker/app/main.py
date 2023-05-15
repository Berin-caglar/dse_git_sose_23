#!flask/bin/python
from flask import Flask, jsonify, abort, request
app = Flask(__name__)

@app.route('/')
def index():
    return "Dies ist die Kursverwaltung zu DSE."

students = [
    {
        'id': 1,
        'name': 'Franz',
        'semester': 3,
        'aktiv': True
    },
    {
        'id': 2,
        'name': 'Lydia',
        'semester': 1,
        'aktiv': False
    }
]

@app.route('/api/studierende', methods=['GET'])
def get_students():
    return jsonify({'studierende': students})


@app.route('/api/studierende/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = [student for student in students if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    return jsonify({'student': student[0]})

@app.route('/api/studierende', methods=['POST'])
def create_student():
    if not request.json or not 'name' in request.json:
        abort(400)
    student = {
        'id': students[-1]['id'] + 1,
        'name': request.json['name'],
        'semester': request.json.get('semester', 0),
        'aktiv': request.json.get('aktiv', False)
    }
    students.append(student)
    return jsonify({'student': student}), 201

@app.route('/api/studierende/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = [student for student in students if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' not in request.json:
        abort(400)
    student[0]['name'] = request.json.get('name')
    return jsonify({'student': student[0]})


@app.route('/api/studierende/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = [student for student in students if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    students.remove(student[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)