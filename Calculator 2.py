#Team Members
#Sandile, Liyema, Mbuso
#cheese
#Sandile did the Inputs
greet = "Welcome to THE Calculator"
print(greet)

menu = "1.multiply 2.division 3.subtraction 4.addition 5.modulas"
print(menu)
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
    c = a - b
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
#I used the if choose because Sandile define the variable choose,
#This helps as you can see below we said if choose == 1, this means that if the user chose
# 1 when asked what operator to use it will multiply num1 and 2. if you chose elif choose ==2 this means
# that if the user chose 2 when asked what operator to use it will divide num1 and num2. 

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

<<<<<<< HEAD

#67
=======
#67
#This calculator works great and it is the best
>>>>>>> fa7712c5bd5109c462043389c4c7c344421379d4
