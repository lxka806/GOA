from django.shortcuts import render

# Create your views here.
students_database = [
    {"id": 0, "name": "ნიკა", "age": 15, "grade": 9},
]

def all_students(req):
    return render(req, "index.html", {
        'students': students_database
    })

def student_with_id(req, id):
    if 0 <= id < len(students_database):
        student = students_database[id]
    else:
        student = None

    return render(req, "student.html", {
        "student": student
    })