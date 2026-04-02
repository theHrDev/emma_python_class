print("Welcome to my calculator")
def calculator():
    print("What do you want to do?: ")
    menu = input("1.Addition 2.Subtraction 3.Division ")
    if menu == "1":
        addition()
    elif menu == "2":
        subtraction()
    elif menu == "3":
        division()
    else:
        print("invalid input")
        
        
def addition():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first + second
    print(result)
    
def subtraction():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first - second
    print(result)
    
def division():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first / second
    print(result)
    
    
calculator()


