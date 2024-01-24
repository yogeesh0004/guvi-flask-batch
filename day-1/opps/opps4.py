#single level inheritance without constructor
class Parent:
    family_name="shettys"

    def property(self):
        print("Parent property")

    def business(self):
        print("Parent business")

class Child(Parent):

    child_name="Chandan"

    def childproperty(self):
        print("Child property")

    def childbusiness(self):
        print("Child business") 

# obj=Child()
# obj.property()
# obj.business()
# obj.childproperty()
# obj.childbusiness()
# print(obj.family_name)
# print(obj.child_name)


obj2=Parent()
obj2.business()
obj2.property()

obj2.childproperty()