class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}, "

class Developer(Employee):
        def __init__(self, name, employee_id, salary, programming_language):
            super().__init__(name, employee_id, salary)
            self.programming_language = programming_language
        
        def get_details(self):
            return f"{super().get_details()}, Programming Lang: {self.programming_language}"
        

class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def get_details(self):
         return f"{super().get_details()}, Team Size: {self.team_size}"
    
def show_employee_details(emp):
     print(emp.get_details())


dev_emp = Developer("Anil Yadav", 1001, 80000, "Python")

mgr_emp = Manager("Anil", 501, 90000, 10)

show_employee_details(dev_emp)
show_employee_details(mgr_emp)