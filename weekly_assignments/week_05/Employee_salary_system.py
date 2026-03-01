class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def calculate_salary(self):
        return self.base_salary + self.base_salary * 0.5


class Developer(Employee):
    def calculate_salary(self):
        return self.base_salary + self.base_salary * 0.3


class Intern(Employee):
    def calculate_salary(self):
        return self.base_salary * 0.5


employees = [
    Manager("Alice", 5000),
    Developer("Bob", 4000),
    Intern("Charlie", 2000)
]

for emp in employees:
    print(f"{emp.name} - Salary: {emp.calculate_salary()}")