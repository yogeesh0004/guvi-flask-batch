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
        print("i have set the values successfully for",self.employeeName)

    def employeeDetails(self):     
        print(f'\nCompany name is {self.company}\nEmployee Name is {self.employeeName}\nEmployee age is {self.employeeAge}\nEmployee role is {self.employeeRole}\nEmployee salary is {self.employeeSalary}')
        

emp1=Employee("Rohan",25,"full stack developer",30000)
emp2=Employee("Anees",25,"backend  developer",50000)

emp1.employeeDetails()
emp2.employeeDetails()


emp1.employeeAge=100
emp1.employeeDetails()


