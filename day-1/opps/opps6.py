class Employee:
    # initializing the constructor
    company="Infosys"
    def __init__(self,employeeName,employeeAge,employeeRole,employeeSalary): 
        # print("i am a constructor i will get called defaultly whenever object is getting created")
        #contructor which will set your values for the specific object this we need to do it
        self.employeeName=employeeName
        self.employeeAge=employeeAge
        self.employeeRole=employeeRole
        self.employeeSalary=employeeSalary
        print("i have set the values successfully")

    def employeeDetails(self):
        return f'\nCompany name is {self.company}\nEmployee Name is {self.employeeName}\nEmployee age is {self.employeeAge}\nEmployee role is {self.employeeRole}\nEmployee salary is {self.employeeSalary}'

    
    @classmethod
    def changeCompany(self,cls):
        self.company=cls
        print("Your company is changed to ",{self.company})






emp1=Employee("Rohan",25,"full stack developer",30000)
emp2=Employee("Anees",25,"backend  developer",50000)

employee1=emp1.employeeDetails()
employee2=emp2.employeeDetails()

print(employee1)
print(employee2)

emp1.changeCompany("Infosys Limited")

employee1=emp1.employeeDetails()
employee2=emp2.employeeDetails()

print(employee1)
print(employee2)
# emp2.changeCompany("Infosys Limited")
# print(emp1.employeeDetails())
# print(emp2.employeeDetails())

# salary=emp1.employeeSalary+emp2.employeeSalary #accessing the values from data members of the class
# print(salary)