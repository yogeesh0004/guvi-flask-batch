class Human: #classname is Human
    # creating the data members of the class
    human_name="Indian"
    age=75
    category=['male','female']

    #methods of the class Human
    def humanDetails(self):
        print(f"Human name is {self.human_name}\nHuman age ratio is {self.age}\nHuman has two category {self.category}")


    def greeting(self):
        print("Good morning have a nice day at GUVI")



obj1=Human() #object1
print(type(obj1))
print(obj1.human_name)
print(obj1.age)
print(obj1.category)


obj2=Human() #object1
obj2.human_name="Anees"
obj2.age=30
print(obj2.human_name)
print(obj2.age)
print(obj2.category)

obj1.humanDetails()
obj1.greeting()
print("\n")
obj2.humanDetails()
obj2.greeting()