class Employee:
    def __init__(self, name, salary, project):
        self.name=name
        self.salary=salary
        self.project=project
    def show(self):      
        print("Name:",self.name,'Salary:',self.salary)
    def work(self):
        print(self.name, 'is working on', self.project)
emp = Employee('Ram', 8000, 'Mobile application')
emp.show()
emp.work()

'''Output:
Name: Ram Salary: 8000
Ram is working on Mobile application '''