import json

class Student:
    def __init__(self, name, id, scores):
        self.name = name
        self.id = id
        self.scores = scores
    def average_score(self):
        return sum(self.scores) / len(self.scores)
    def __str__(self):
        return f"Student(name={self.name}, id={self.id}, average_score={self.average_score():.2f})"

Student1 = Student("Alice", "S001", [85, 90, 78])
Student2 = Student("Bob", "S002", [92, 88, 95])

json_data1 = json.dumps(Student1.__str__())
json_data2 = json.dumps(Student2.__dict__)
print(json_data1)
print(json_data2)