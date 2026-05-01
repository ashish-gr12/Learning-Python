class Employee :
    company = "HP"
    def __init__(self,salary,name,bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
    
    def get_salary(self) :
        return self.salary
    
    def get_info(self) :
        print(f"The name is {self.name} , salary is {self.salary} and bond is for {self.bond} years")

e1 = Employee(56100,"Sai",3,"BharatForge")
e1.get_info()
print(e1.company)
print(Employee.company)
print(e1.get_salary())

# Object Introspection - Returns all the instances and methods of a particular object
print(dir(e1))