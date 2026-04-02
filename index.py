print("Welcome to my calculator")
def calculator():
    print("What do you want to do?: ")
    menu = input("1.Addition 2.Subtraction ")
    if menu == "1":
        addition()
    elif menu == "2":
        subtraction()
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
calculator()


