#create a class "employee" and add salary and increnement properties to it.
class Employee:
    def __init__(self, salary):
        self.salary = salary
        self.increment = 0  # percentage

    def set_increment(self, percent):
        self.increment = percent

    def get_salary_after_increment(self):
        return self.salary + (self.salary * self.increment / 100)


# Example usage
emp = Employee(30000)
emp.set_increment(10)

print("Original Salary:", emp.salary)
print("Salary after increment:", emp.get_salary_after_increment())
