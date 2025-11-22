# Q1. Write a program that asks the user for their name and age, then prints a sentence.
'''
name = str(input("Enter your Name: "))
age = int(input("Enter your age: "))

print("Hello",name,", You are", age, "years old.")
'''

# Q2. Take two numbers as input from the user and print their.Sum, difference, product, and quotient.
'''
a = float(input("Enter your first number:"))
b = float(input("Enter your first number:"))

sum = a+b
difference = a-b
product = a*b
quotient = a/b

print("The sum of ", a, "and", b, "is: ", sum)
print("The difference of ", a, "and", b, "is: ", difference)
print("The product of ", a, "and", b, "is: ", product)
print("The quotient of ", a, "and", b, "is: ", quotient)

'''
# Q3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.
'''
a = int(input("Enter your first integer: "))
b = int(input("Enter your second integer: "))
c = float(input("Enter your third a decimal number: "))

avg = float(a+b+c)/3
print("The average of number that you entered is: ", avg, ".")
'''

# a = str(input("Enter your first integer: "))
# b = int(a)
# print(type(b), b)
# c = float(b)
# print(type(c), c)
# d = str(c)
# print(type(d), d)

#Evalute and print the result 
'''
x =10+3*2**2
print(x) #these are operaters which will operate with their order arrange. Ans should be 22.
'''
'''
#swaping the two number entered by user input.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# before swaping
print("a= ",a)
print("b= ",b)

#swaping
a,b = b,a

#After swaping print the numbers

print("a= ",a)
print("b= ",b)
'''

'''
#Convert celcious temprature into farenhite

a = str(input("Enter Celcious temprature: "))
celsiustemp = float(a)
FahrenheitTemp = (celsiustemp*(9/5))+32

print("In Farenhite temp is: ", FahrenheitTemp)
'''
'''
# Take radius from user and calculate the Area of the circle.
radius = float(input("Enter the Radius of the Circle: "))
PI = 3.14
area = PI*(radius**2)
print("The Area of the Circle is: ", area)
'''
'''
#Calculate the simple interest
p = float(input("Enter the principal ammount: "))
r = float(input("Enter the Interest Rate: "))
t = float(input("Enter Time duration: "))
si = (p*r*t)/100

print("Based on getting details , Simple interest is: ", si)
'''

'''
# seprate the ntegerpart and fractional part by taking input nuber by an user
num = float(input("Enter a decimal number with two places after decimal: "))
integer = int(num)
fractional = num - integer
print("Integr part is: ", integer, ",and Fractional part is: ", fractional)
'''
