class Employee:
    empno = 0
    def __init__(self, n, des, sal):
        self.name = n
        self.designation = des
        self.salary = sal
        Employee.empno += 1
    def display(self):
        print(self.name, "\t", self.designation, "\t", self.salary)
n = int(input("Enter the number of employees: "))
print("Enter employee details:")
employees = []
for i in range(n):
    print(f"Employee {i+1}:")
    name = input("Name: ")
    designation = input("Designation: ")
    salary = float(input("Salary: "))
    emp = Employee(name, designation, salary)
    employees.append(emp)
    print()
print("Name\tDesignation\tSalary")
for emp in employees:
    emp.display()
print("Total number of employees: ", Employee.empno)