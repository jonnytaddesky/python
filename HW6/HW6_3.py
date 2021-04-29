class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary = string.split('-')
        return cls(first_name, last_name, salary)


emp1 = Employee('John', 'Smith', 6000)
print(emp1.first_name)
print(emp1.last_name)
print(emp1.salary)
emp2 = Employee.from_string('Artem-Syvohlaz-10000')
print(emp2.first_name)
print(emp2.last_name)
print(emp2.salary)
