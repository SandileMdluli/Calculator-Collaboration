#Team Members
#Sandile, Liyema, Mbuso

greet = "Welcome to THE Calculator"
print(greet)

num1 = float(input("Enter a number:"))
num2 = float(input("Enter a number:"))

choose = int(input("What operation do you want to use"))

def multiply(a,b):
    c = a * b
    return c

def division(a,b):
    c = a / b
    return c

def subtraction(a,b):
    c = a * b
    return c

def addition(a,b):
    c = a + b
    return c

def modulas(a,b):
    c = a % b
    return c

if choose == 1:
    print(multiply(num1,num2))
elif choose ==2:
    print(division(num1,num2))
elif choose ==3:
    print(subtraction(num1,num2))
elif choose ==4:
    print(addition(num1,num2)) 
elif choose ==5:
    print(modulas(num1, num2))
