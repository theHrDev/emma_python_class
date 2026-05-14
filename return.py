# Return statement
# to exit a function
# to return a value to the caller

# def my_func():
#     print("name")
#     return "hello"
#     print("Welcome")

# print(my_func())
# print(my_func())

# a = my_func()
# print(a)

# def square(num): 
#     return num * num

# # square(4)
# print(square(10)) #100
# print(square(2))  #4
# print(square(6)) #36



def calculator(num1,num2,opr):
    if opr == "+":
        return num1 + num2
    elif opr == "-":
        return num1 - num2
    elif opr == "*":
        return num1 * num2
    elif opr == "/":
        if num1 == 0 or num2 == 0:
            return "You cannot divide with zero"
        else:
            return num1 / num2    
        
    else:
        return "invalid operator"    
    
    

print(calculator(2,3,"+"))  #5
print(calculator(6,3,"-"))  #3
print(calculator(5,3,"*"))  #15
print(calculator(0,10,"/"))  #3



# 70 - 100  = A
# 60 - 69 =  B
# 50 - 59 = C
# 45 - 49   = D
# 40 - 44 = E
# 0 - 39 = F

# you score (score/total) * 100
# you score 20 percent out of 100 which is grade F

def grade_student(score,total):
    pass


grade_student(20,100)
grade_student(60,120)