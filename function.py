# Parameterized function

# variable + function
# DRY
# def greet_emma():
#     name = "Emmanuel"
#     print(f"Hi, how are you doing {name}")
    
# greet_emma()

# def greet_tolu():
#     name = "Tolu"
#     print(f"Hi, how are you doing {name}")
    
# greet_tolu()
# parameter and Argument
def greet_people(name,age,dept="CSC"):
    print(f"Hi, how are you doing {name} and your age is {age}, you are in {dept} department")

user_name = input("Enter your name: ") 
user_age = int(input("Enter your age: "))
greet_people(user_name,user_age)


# Assignment
# price and tax
# total_amount = price + (price * tax)