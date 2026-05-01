# A class is a blueprint of an object .

class Employee:
    company = "HP"
    
    def get_salary(self):
        return 56100
    
e1 = Employee()
print(e1.get_salary())
e2 = Employee()
print(e2.get_salary())
print(e2.company)