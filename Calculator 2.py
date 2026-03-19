#Team Members
#Sandile, Liyema, Mbuso

#Sandile did the Inputs
greet = "Welcome to THE Calculator"
print(greet)

#User enters number
num1 = float(input("Enter a number:"))
num2 = float(input("Enter a number:"))

#User chooses what operator they want to enter
choose = int(input("What operation do you want to use"))

#Liyema did the menu to define the operators
#Mutiplication funtctio
def multiply(a,b):
    c = a * b
    return c

#Division function
def division(a,b):
    c = a / b
    return c

#Subtraction function
def subtraction(a,b):
    c = a * b
    return c

#Addition Function
def addition(a,b):
    c = a + b
    return c

#Modulas function
def modulas(a,b):
    c = a % b
    return c

#Mbuso did IF to operate the calculator
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

