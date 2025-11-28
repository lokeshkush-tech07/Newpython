'''find a word from attached text file and print this with numberline also'''

# word = "codes"
# line = 1
# with open("sample.txt", "r") as f:
#     while True:
#         data =  f.readline()
#         if word in data:
#            print(f"{word}, founded in line {line}")
#            break
#         else:
#            pass
#         line +=1

''' Q1. Create a program that:
    i. open a file "names.txt" in write mode.
    ii. write 5 names (one per line) entered by the user.
    iii. Then Opens the same file in read mode and prints all names'''

# f = open("names.txt", "w")
# for i in range(5):
#     names = input("Enter name: ")
#     f.write(names + "\n")
# f.close()

# f = open("names.txt", "r")
# print(f.read())

'''create a program that:
  opens a file "log.txt" in append mode
  add a new log entry (like"program run successfully!")
  open the files in read mode and prints all logs'''

# with open("log.txt", "a") as f:
#     f.write("program run successfully!\n")

# with open("log.txt", "r") as f:
#     print(f.read())

'''create a program that
    has a list of numbers : [5,10, 15, 20, 25]
    uses a list comprehension to create a new list with only numbers greater than 15
     print the new list '''
# list = [5,10, 15, 20, 25]
# new_list = [num for num in list if num>= 15]
# print(new_list)

''' Q4. Create a Python dictionary of 3 cities and their populations.Save it to "cities.json".
         Then load the JSON and print each city and its population
         Ask the user for a new city & its population - update this info in the json file'''
import json

# #Create a dictionary of 3 cities
# cities = {
#     "Delhi": 7886354,
#     "Mumbai": 6748323,
#     "Hyderabad": 8777653
# }
# #  Save it into cities.json
# with open("cities.json", "w") as f:
#     json.dump(cities, f)

# #Load the JSON file
# with open("cities.json", "r") as f:
#     data = json.load(f)

# #Print each city and population
# print("Current cities and populations:")
# for city, pop in data.items():
#     print(city, ":", pop)

# # Ask user for new city
# new_city = input("Enter a new city name: ")
# new_pop = int(input("Enter its population: "))

# # Add to dictionary
# data[new_city] = new_pop

# with open("cities.json", "w") as f:
#     json.dump(data, f)

# print("New city added successfully!")

'''Q5. Write a program that tries to open in read mode.If the file does not exist, catch the 
exception and print "Filenotfound!".'''

try:
    f  = open("new.txt")
    print(f.read())

except FileNotFoundError:
    print("Filenotfound!")

