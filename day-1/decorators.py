
# def enrolled(student):#3
#     def enroll():#5
#         print("Yes this student has been enrolled")#6
#         student("Anees")#7
#     return enroll#4

# @enrolled#2
# def student(name):#8
#     print("student name is ",name)#9

# student()#1

def Orders(handleRequest):
    def takeOrder():
        print("Order is saved in db")
        handleRequest(1001)
        print("Order is placed....")
    return takeOrder

@Orders
def handleRequest(id):
    if id==1001:
        print("Success")
    else:
        print("Failure")


# handleRequest()
        
Orders(1001)