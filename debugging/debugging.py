def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    total = 0
    numcount = grades.count(None)
    for num in grades:
        if num == None:
            break
        total += num
    average = total / (len(grades) - numcount)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'}, {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]

def collect_grades(students):
    grades = []
    for student in students:
        name, grade = process_student(student)
        grades.append(grade)
    return grades

grades = collect_grades(students)
print(average_grade(grades))