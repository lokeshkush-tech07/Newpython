# Q1. Ask the user for a string and check whether it is a palidrome or not. hint use reverse.
# while True: 
#     word1 = str(input("Write a word for checking palidrome or not: "))
#     word2 = word1[::-1]
#     print("reversed: ", word2)

#     if word1 == word2:
#         print("Yes It is a palidrome!")
#         break
#     else:
#         print("Not a palidrome, Try again")

# Q2.Given a list of integers compute the average of all numbers in the list.

#list = [3, 5, 6, 3, 1, 8, 9, 6, 4]
# sum = 0
# count = 0

# for num in list:
#     sum += int(num)
#     count += 1

#     avg = sum/count
# print(avg)

# Q3. Input two list of integers from the user. merge them into one list and sort the reslt.
# list1 = list(map(int, input("Enter numbers for the first list separated by spaces:").split()))
# list2 = list(map(int, input("Enter numbers for the second list separated by spaces:").split()))

# merge_list = list1+list2

# new_list = merge_list.sort()
# print("Here is sorted new list:", merge_list)

# Q4. given a tuple of integers create:
#     A tuple of all even numbers
#     A tuple of all odd numbers

# tup = (3, 4, 2, 7, 1, 4, 8, 6, 9, 1)

# even_list = []
# odd_list = []

# for num in tup:
#     if num % 2 == 0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)

# even_tuple = tuple(even_list)
# odd_tuple = tuple(odd_list)

# print("All Even tuple: ", even_tuple)
# print("All Odd tuple: ", odd_tuple)

# Q5.Creat a dictionary where:
#    keys = student names
#    values = marks(integer)

#    write a menu-based program where user presses a key ('A', 'B', 'C', "D")
#    depending on the operation they want to perform on the dictionary:


# students = {"Lokesh":915, "Adarsh":945, "Golu":856}     # dictionary for name → marks

# while True:
#     print("\nMenu:")
#     print("A - Add a student")
#     print("B - Update marks")
#     print("C - Search for a student")
#     print("D - Display all students and marks")
#     print("E - Exit")

#     choice = input("Enter your choice: ").upper()

#     # A - Add a student
#     if choice == "A":
#         name = input("Enter student name: ")
#         marks = int(input("Enter marks: "))
#         students[name] = marks
#         print("Student added successfully!")

#     # B - Update marks
#     elif choice == "B":
#         name = input("Enter student name to update: ")
#         if name in students:
#             new_marks = int(input("Enter new marks: "))
#             students[name] = new_marks
#             print("Marks updated!")
#         else:
#             print("Student not found.")

#     # C - Search for a student
#     elif choice == "C":
#         name = input("Enter student name to search: ")
#         if name in students:
#             print(f"{name} → {students[name]} marks")
#         else:
#             print("Student not found.")

#     # D - Display all students
#     elif choice == "D":
#         if not students:
#             print("No students in the dictionary.")
#         else:
#             print("\nAll Students:")
#             for name, marks in students.items():
#                 print(f"{name}: {marks}")

#     # E - Exit program
#     elif choice == "E":
#         print("Exiting program...")
#         break

#     else:
#         print("Invalid choice. Please try again.")


# Q6. create a dictionary of fuits name and maping there length and show them wih values like{"Apple":5, "Banana":6}

# fruits = ["Apple", "Banana", "Orange", "Kiwi", "Mango", "Lichi"]
# # firstly we are create a empty ditionary with name length okay
# name_length = {}
# for name in fruits:
#     name_length[name] = len(name) 
# print(name_length)


# Q7. Take a string input from user and print the number of spaces of the string.
# sentence = str(input("Enter a short sentence: "))
# count = 0

# for ch in sentence:
#     if ch == " ":
#         count +=1
# print("Number of spaces: ", count)

# Q8. Write a program to check wheather two lists share no common elements.
# list1 = [5, 4, 2, 8, 1]
# list2 = [9, 3, 6]

# for ch in list1:
#     if ch in list2:
#         print("Share common list")
#         break
# else:
#     print("Share no common list")

# Q9. Given a list, print all elements that appear more than once in the list.

# list = [4,2,2,8,5,3,8]
# new_list = []

# for num in list:
#     if num in new_list:
#         print
#     else:
#         new_list.append(num)
# print("This is the new list without dubplicate: ", new_list) 

