'''
There are two ways to assign values to properties of a class.

Assign values when defining the class.
Assign values in the main code.
'''

class Employee:

    #defining initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return self.salary * 0.2

    def salaryPerDay(self):
        return self.salary / 30


