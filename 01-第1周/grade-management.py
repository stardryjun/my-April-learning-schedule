import json

students = [{'Name' : 'Alice', 'Grade' : 7 , 'Class' : 'Seven', 'Score' : 10}]
students.append({'Name' : 'Bob', 'Grade' : 7 , 'Class' : 'Seven', 'Score' : 9})
students.append({'Name' : 'Charlie', 'Grade' : 7 , 'Class' : 'Seven', 'Score' : 8})
students.append({'Name' : 'David', 'Grade' : 7 , 'Class' : 'Seven', 'Score' : 7})
students.append({'Name' : 'Eve', 'Grade' : 7 , 'Class' : 'Seven', 'Score' : 6})
students.remove({'Name' : 'David', 'Grade' : 7 , 'Class' : 'Seven', 'Score' : 7})
students.sort(key=lambda x: x['Score'], reverse=True)

average_score = sum(student['Score'] for student in students) / len(students)
highest_score = max(student['Score'] for student in students)
lowest_score = min(student['Score'] for student in students)
pass_rate = sum(1 for student in students if student['Score'] >= 6) / len(students) * 100

json.dump(students, open('01-第1周/students.json', 'w'), indent=4)
students = json.load(open('01-第1周/students.json', 'r'))
