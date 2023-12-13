class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self, display_option=0):
        if display_option % 3 == 0:
            print("Name : ", self.name)
        elif display_option % 3 == 1:
            print("Salary: ", self.salary)
        elif display_option % 3 == 2:
            print("Department: ", self.department)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Tasks with status {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    """Class representing a manager, inheriting from Employee"""
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        Manager.mgr_count += 1

    def display_employee(self, display_option=0):
        if display_option % 3 == 0:
            print("Name : ", self.name)
        elif display_option % 3 == 1:
            print("Salary: ", self.salary)
        elif display_option % 3 == 2:
            print("Department: ", self.department)

    def display_man_count(self):
        "Displays the number of managers"
        print(f"Total number of manager(s) is {Manager.mgr_count}")


manager1 = Manager("Popescu Ion", 60000, "D12")
manager2 = Manager("Adrian Manea", 70000, "D12")
manager3 = Manager("Simionescu Raul", 80000, "D12")
manager4 = Manager("Darius Dobrea", 90000, "D12")

employee1 = Employee("Sabina Cristiano", 50000)
employee2 = Employee("Trifescu Iustin", 55000)

for obj in [manager1, manager2, manager3, manager4, employee1, employee2]:
    obj.display_employee(10)  

employee1.display_emp_count()
manager1.display_man_count()
