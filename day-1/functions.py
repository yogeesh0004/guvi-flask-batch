# def greeting(name):
#     print("Good Morning",name)

# names=["lalith","manant","yogesh","anees"]
# for i in names:
#     greeting(i)

# def sum(a,b,c=10):
#     d=a+b+c
#     return d

# g=sum(10,20,30)

# z=100
# print(z+g)


# args and kwargs 

# def sorting(*args):
#     # print(args)
#     for i in args:
#         print(i)

# sorting([1,2,3],[4,5,6,7],[8,9,10])

def employeeDetails(name,*args,**mydict):
    print(type(mydict))
    for key,value in mydict.items():
        print(key,value)
    print("\n")
    print(args)
    print("\n")
    print(name)


mydict={
    "employeeName":"Rohan",
    "employeeSalary":15000,
    "isActive":True,
    "role":["frontend dev","backend dev"],
    "hobbies":('playing','dancing','singing'),
    "skills":{"python","flask"}
}
args=[1,2,3,4,5,6],[34,5,6,7]

name="guvi"

employeeDetails(name,*args,**mydict)
