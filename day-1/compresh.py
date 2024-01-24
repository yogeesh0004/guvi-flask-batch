# comprehensions
# mylist=[]
# for i in range(11):
#     print(i)
#     if i%2==0:
#         mylist.append(i)

# print(mylist)

# mylistc=[i for i in range(21) if i%2==0]
# print(mylistc)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [x for x in numbers if x % 2 == 0]
# print(evens)
# # Result: evens = [2, 4, 6, 8, 10]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [x for x in numbers]
# print(evens)

# set comprehensions
# alphabet=['a','b','c','d','e','f','g']
# alphabets={i for i in alphabet if i!='b'}
# print(alphabets)


# 0 : "name 0",
# 1 : "name 1"
# 2 : "name 2"


# dictionary_compresss={i:f'Name {i}' for i in range(1,11) if i%2==0}
# print(dictionary_compresss)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
evens = (x for x in numbers)
print(list(evens))