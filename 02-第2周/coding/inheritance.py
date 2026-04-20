class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Person(my name is {self.name})"
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name
        return False

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
    def __repr__(self):
        return f"Employee(my name is {self.name}, id: {self.employee_id})"
    def __eq__(self, other):
        if isinstance(other, Employee):
            return super().__eq__(other) and self.employee_id == other.employee_id
        return False

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
    def __repr__(self):
        return f"Manager(my name is {self.name}, id: {self.employee_id}, department: {self.department})"
    def __eq__(self, other):
        if isinstance(other, Manager):
            return super().__eq__(other) and self.department == other.department
        return False

person1 = Person("Alice")
employee1 = Employee("Bob", "E123")
manager1 = Manager("Charlie", "M456", "Sales")
person2 = Person("Bob")
employee2 = Employee("Bob", "E123")
manager2 = Manager("Charlie", "M789", "Sales")
print(person1,person2)
print(employee1,employee2)
print(manager1,manager2)
print(person1 == person2)
print(employee1 == employee2)
print(manager1 == manager2)