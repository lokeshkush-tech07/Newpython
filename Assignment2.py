# Q1.write a program that takes salary as input. Using conditional statmemts, calcilate the final tax 
#    rate based on these rules:
#    i. If salary < 30,000 then 5%
#    ii. If salary is 30,000 to 70,000 then 15%
#    iii. If salary > 70,000 then 25%

# salary = int(input("Enter your salary: "))

# if salary < 30000:
#     print("You have to pay tax : ", salary*(5/100))
# elif salary >= 30000 and salary <= 70000:
#     print("You have to pay tax : ", salary*(15/100))
# else :
#     print("You have to pay tax : ", salary*(25/100))


# Write a function that takes two integers a and b and prints all even numbers between them(inclusive).

# def num(a,b):
#     for number in range(a, b+1):
#         if number % 2 == 1:
#             print(number)

# a = int(input("Enter your first num: "))
# b = int(input("Enter your second num: "))

# num(a,b)

# Q3.Write a function that prints the digits of a number, n.

# def number(n):
#     for digit in str(n):
#         print(digit)
# n = int(input("Enter the number : "))

# number(n)

# Q4.Write a function to return the count the number of digit in a number, n.

# def num(n):
#     count = len(str(n))
#     return count

# n = int(input("Enter the number: "))
# print("The number of total digits is:", num(n))

# Q5.write a function to return the sum of digits of a nmber, n.

# def num(n):
#     total = 0
#     for ch in str(n):
#         total += int(ch)
#     return total
# n = int(input("Enter the number: "))
# print("the sum of all digit of given number is: ", num(n))
    
# Q6. Write a program to print all nmbers from 1 to 100 that are divisible by both 3 and 5 both.
# i = 1
# while (i <= 100):
#     if(i % 15 == 0):
#         print(i)
#     i +=1

# Q7. Design a program to continously input a number nn from user 
#     & print if it is positive or negative until the user enters "Quit".

# while True:
#     user_input = input("Enter a number or if you want exit then type quit: ")
#     if user_input == "quit":
#         break
#     n = int(user_input)
#     if n < 0:
#         print("Entered number is negative: ")
#     elif n > 0:
#         print("Entered number is positive: ")
#     else:
#         print("Entered number is 0")

# Q8. lets create a simple calculator that performs arithmatic operations. Create a function calculater(a,b, operation)
#     that performs addition, substraction, multiplication, or divsion based on the operation parameter.
#    [operation parameters can have values '+', '-', '*' & '/']

















# Q9. Write a function is_prime(n) that returns True if n is prime numberand flasse otherwise, using a loop.












# Q10. Let's create a "Number Guessing Game". Given a secret number (already decided by you), 
#      write a program that asks the user to guess it and prints:
#     i. "To high" if the guess is above the number
#     ii. "To low" if the guess is below
#    iii. "Correct!" if the guess matches

# while True:
#     user_input = input("Enter a number btw 1 to 50 or if you want exit then type quit: ")
#     if user_input == "quit":
#         break
#     n = int(user_input)
#     a = 36
#     if n == a:
#         print("Correct!")
#         break
#     elif n > a:
#         print("To high")
#     else:
#         print("To low")