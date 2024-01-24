# 1)write a python program to order the food in the swiggy display the menu for the user 1. Dosa2. Idli3. Pizza4. Burgers5. Chicken6. Biryani7. Ice Cream8. Place order#calling to swigy........example : press 1 to order Dosa and so onif i press 4. your order is been added to cartif i press 6. your order is been added to the cart if i press 8 your order is placed. items : list your total amount.

def menu():
    print("Welcome to swiggy order your items:\n")
    print("Press 1 for order : Dosa ")
    print("Press 2 for order : Idli ")
    print("Press 3 for order : Pizza ")
    print("Press 4 for order : Burger ")
    print("Press 5 for order : Chicken  ")
    print("Press 6 for order : Biryani ")
    print("Press 7 for order : Ice cream ")
    print("Press 8 for final order : order ")

items=[]
amount=[]

def swiggy():   
    menu()
    n=int(input("Enter the order number: "))
    if(n>=1 and n<=8):
        if n==1:
            item="Dosa"
            items.append(item)
            amount.append(80)
            print(f"Your order item {item} is been added to the cart ")
            swiggy()
        elif n==2:
            item="Idli"
            items.append(item)
            amount.append(30)
            print(f"Your order item {item} is been added to the cart ")
            swiggy()
        elif n==3:
            item="Pizza"
            items.append(item)
            amount.append(300)
            print(f"Your order item {item} is been added to the cart ")
            swiggy()
        elif n==4:
            item="Burger"
            items.append(item)
            amount.append(150)
            print(f"Your order item {item} is been added to the cart ")
            swiggy()
        elif n==5:
            item="Chicken"
            items.append(item)
            amount.append(200)
            print(f"Your order item {item} is been added to the cart ")
            swiggy()
        elif n==6:
            item="Biryani"
            items.append(item)
            amount.append(150)
            print(f"Your order item {item} is been added to the cart ")
            swiggy()
        elif n==7:
            item="Ice cream"
            items.append(item)
            amount.append(100)
            print(f"Your order item {item} is been added to the cart ")
            swiggy()
        else:
            print("thanks for choosing swiggy.....")


    else:
        print("Please select the correct order number")
        swiggy()

swiggy()
print("Your Ordered items are ",items)
print("Your Ordered items total amount is ",sum(amount))