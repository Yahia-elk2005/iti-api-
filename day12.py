# ana Yahia Ahmed 
name = "Yahia" #string
age = 20 #int
skills = ["Python","Frontend", "Machine Learning"] #list
info = {"location": "Egypt", "role": "Developer"} #dict

print(type(name))        #  'str'
print(type(age))         #  'int'
print(type(skills))      #  'list'
print(type(info))        #  'dict'


skills.append("Deep Learning")
print(skills) #to see if it worked or not 


class Employee:
    title = "PythonTech"  

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def displayInfo(self):
        return f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

    
    def yearSalary(self):
        return self.salary * 12

    
    @classmethod
    def getCompany(cls):
        return cls.title

    
    @staticmethod
    def validSalary(salary):
        return salary >= 6000


emp1 = Employee("Omar", "Engineering", 26500)
emp2 = Employee("jana", "Marketing", 5800)

print(emp1.displayInfo())
print(emp2.displayInfo())


print(f"Yearly Salary: {emp1.yearSalary()}")
print(f"Is salary valid? {Employee.validSalary(emp1.salary)}")


print(f"Company Name: {Employee.getCompany()}")