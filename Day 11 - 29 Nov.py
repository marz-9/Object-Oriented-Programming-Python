class Employee:
    def __init__(self, name, ID, salary, department):
        self.name=name
        self.ID=ID
        self.salary=salary
        self.department=department
        
    def set_department(self,new_department):
        self.department=new_department
    def calc_salary(self,hoursW):
        self.hoursW=hoursW
        if (self.hoursW > 50):
            overtime=self.hoursW-50
            Over_amount=(overtime*(self.salary/50))
            total=self.salary+Over_amount
            return total
        else:
            return self.salary
    def __str__(self):
        return "Employee name: {}. ID: {}. Salary: ${}. Department: {}.".format(self.name, self.ID,self.salary,self.department)

emp1=Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2=Employee("JONES", "E7499", 45000, "RESEARCH")
emp3=Employee("MARTIN", "E7900", 50000, "SALES")
emp4=Employee("SMITH", "E7698", 55000, "OPERATIONS")

print(emp1)
print(emp2)
print(emp3)
print(emp4)
emp4.set_department("SALES")
print(emp4)
print("The salary of ", emp1.name, " before is ",emp1.salary, ".Because of overtime hours it became: ",emp1.calc_salary(55))
print("The salary of ", emp2.name, " before is ",emp2.salary, ".No overtime ",emp2.calc_salary(40))
print("The salary of ", emp3.name, " before is ",emp3.salary, ".No overtime",emp3.calc_salary(50))
print("The salary of ", emp4.name, " before is ",emp4.salary, ".No overtime",emp4.calc_salary(45))
