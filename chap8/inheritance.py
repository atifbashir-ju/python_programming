class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company = "YouTube"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showlang(self):
        print(f"The name is {self.name} and the language is {self.language}")


# objects
a = Employee("Atif", 50000)
b = Programmer("Ali", 80000, "Python")

a.show()
b.show()
b.showlang()

print(a.company)
print(b.company)
