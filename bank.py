total_balance = 10000

def my_bank():
    print("Welcome to my bank app,What do you want to do")
    menu = input("1.Deposit 2.Withdraw:  ")
    
    if menu == "1":
        deposit()  
    elif menu == "2":
        withdraw() 
    else:
        print("Invalid input")
        
    rerun = input("Do you want to do anything else? 1.yes  2.no: ")
    if rerun == "1":
        my_bank()
    else:
        print("Thanks for using our bank")
        

def deposit():
    global total_balance
    amount = float(input("How much do you want to deposit? ")) 
    total = amount + total_balance
    total_balance = total
    print("Money successfully deposited")
    print(total_balance)

def withdraw():
    global total_balance
    amount = float(input("How much do you want to withdraw? "))
    if amount > total_balance:
        print("insufficient fund")
    else:
        total = total_balance - amount 
        total_balance = total
        print("Money withdrawn successfully")
        print(total_balance)
        
my_bank()
    
    
# def greet():
#     print("welcome")
    
#     repeat = input("Do you want to greet again 1. yes 2.no: ")
#     if repeat == "1":
#         greet()
#     else:
#         print("Bye")
        
# greet()