class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name} - Salary: {self.salary}"

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_info(self):
        return super().get_info() + f" - {self.language}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_info(self):
        return super().get_info() + f" - Team: {self.team_size}"

employees = [
    Developer("Dimitar",2100, "Python"),
    Manager("Georgi", 2800, 5),
    Developer("Ivan", 2500, "C#"),
    Manager("John", 3800, 10)
]

for employee in employees:
    print(employee.get_info())