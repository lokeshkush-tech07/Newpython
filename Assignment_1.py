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
a = int(input("Enter your first integer: "))
b = int(input("Enter your second integer: "))
c = float(input("Enter your third a decimal number: "))

avg = float(a+b+c)/3
print("The average of number that you entered is: ", avg, ".")

