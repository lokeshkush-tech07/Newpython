'''Q1. Create a BankAccount class with attributes account_numbr, owner_name, and balance.
    Add methods to deposit, withdraw, and check_balance.'''

# class BankAccount:

#     def __init__(self, account_number, owner_name, balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance

#     def get_info(self):
#         print(f"Account number: {self.account_number}, Name: {self.owner_name}, Balance: {self.balance}")

#     def deposite(self, ammount):
#         self.balance += ammount
#         print(f"Deposited balance: {ammount}, And New balance is {self.balance} Rupees.")

#     def withdraw(self, ammount):

#         if self.balance < ammount:
#             print(f"Insufficeint funds: {self.balance}")
#         else:
#             self.balance -= ammount
#             print(f"Withdraw Balance: {ammount}, And New balance is {self.balance} Rupees.")

#     def check_balance(self):
#         print(f"Your Ammount Balance is : {self.balance} Rupees.")


# A1 = BankAccount("45678932198","Lokesh",10_000)
# A1.withdraw(11500)
# A1.get_info()


'''Q2. Create a class Book with the following attributes:
      i.Title
     ii.author
    iii.List of reviews

  And add methods to :
    i. add a new review
   ii. count reviews
  iii. display all reviews '''

# class Book:

#     def __init__(self, title, author, list_of_reviews):
#         self.title = title
#         self.author = author
#         self.list_of_reviews = list_of_reviews
#         self.count = 1

#     def get_info(self):
#         print(f"Book Name: {self.title}, Author Name: {self.author}, And Reviews: {self.list_of_reviews}")

#     def new_review(self, review):
#         self.list_of_reviews += f", {review}"
#         self.count +=1

#     def review_count(self):
#         print(f"Number of total given reviews: {self.count}")

#     def display_review(self):
#         print(f"These are the all reviews by Readers:- {self.list_of_reviews}")

    

# B1 = Book("Siblings", "Lokesh", "Excellent")
# B2 = Book("SKC", "Saleem bhaiya", "Best book")
# B1.new_review("very good")
# B1.new_review("Nice")
# f"This is the full details of available Books: {B1.get_info()} \n{B2.get_info()}"
# B1.review_count()
# B2.display_review()

''' Q3. Create a class student with private attibute _name, _roll_no, and _marks. 
Provide getter and setter mehods with validation (e.g, marks cannot be negative, roll number has to be between
1 and 100 and name cannot be empty. )'''

# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.__name = name #private attribute
#         self.__roll_no = roll_no #private attribute
#         self.__marks = marks #private attribute

#     def get_info(self): #function for getting information of indivisual students details
#         print(f"Name: {self.__name}, Roll no: {self.__roll_no}, Marks: {self.__marks}")

# #-----------------------------------------
# # using getter method for indirectly acces
# #-----------------------------------------

#     def get_name(self): #for name
#         return self.__name
    
#     def get_roll_no(self): # for roll no
#         return self.__roll_no
    
#     def get_marks(self): # for marks
#         return self.__marks
    
# #-----------------------------------------
# # Using setter method for modification
# #-----------------------------------------
#     def set_name(self, new_name): #name modificaion
#         if new_name.strip() == "":
#             print("Name cannot be empty !")
#         else:
#             self.__name = new_name

#     def set_roll_no(self, new_roll_no): #Roll no modification
#         if 1<= new_roll_no <= 100:
#             self.__roll_no = new_roll_no
#         else:
#             print("Roll no has to must be btw 1 to 100")

#     def set_marks(self, new_marks): # Marks Modification
#         if new_marks < 0:
#             print("Marks cannot be negative")
#         else:
#             self.__marks = new_marks

# S1 = Student("Lokesh", 33, 358)
# S1.get_info()

'''Functon overriding based question.
create a class shape with a method area()
create subclasses circle, Rectangle, Triangle that override the area method.'''

# class Shape():
#     def area(self):
#         print("Area of the shape is depend upon how is the shape.So go through with\nArea of circle, rectangle and Triangle")

# class circle(Shape):
#     def area(self, r):
#         self.r = r
#         PI = 3.14
#         print(f"Area of the circle is; {PI*(self.r**2)}")

# class Rectangle(Shape):
#     def area(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#         print(f"Area of the recatangle is: {self.length * self.breadth}")

# class Triangle(Shape):
#     def area(self, base, height):
#         self.base = base
#         self.height = height
#         print(f"Area of the Triangle is: {(1/2)*self.base*self.height}")

# S = Shape()
# C = circle()
# R = Rectangle()
# T = Triangle()
# # T.area()
# # C.area(4)
# # S1.area()
# # T.area(2,4)
# S.area()

'''Inheritance based questions..
Create a base class vehicle wih atributes like brand model.
ceate two subclasses car and bike that add extra attributs  seats(in car) and engine__cc(in bike)'''

# class vehicle():
#     def __init__(self, brand, model):
#         self.model = model
#         self.brand = brand

# class car(vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand, model)
#         self.seats = seats

#     def show(self):
#         print(f"Brand name: {self.brand},\nModel name: {self.model}, \nSeats available: {self.seats}")

# class bike(vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc

#     def show(self):
#         print(f"Brand name: {self.brand},\nModel name: {self.model},\nEngine_cc: {self.engine_cc}")

# C = car("Tata", "safari", 5)
# B = bike("Suzuki", "ninja", 360)
# C.show()
# B.show()

''' #Abstraction and use (from abc import ABC , absstraction )
Create an abstract class employee with an abstract method calculate_salary()
create subclasses Intern, FullTimeEmployee and ContractEmployee that implement the method differently.'''

# from abc import ABC, abstractmethod

# class Employee(ABC):

#     @abstractmethod
#     def Calculate_salary(self):
#         pass

# class Intern(Employee):
#     def __init__(self, stipend):
#         self.stipend = stipend

#     def Calculate_salary(self):
#         print(f"The sitpend of a Intern is: {self.stipend}")

# class FullTimeEmoloyee(Employee):
#     def __init__(self, salary):
#         self.salary = salary

#     def Calculate_salary(self):
#         print(f"The salary of a Full Time Emoloyee is: {self.salary}")

# class ContractEmployee(Employee):
#     def __init__(self, rent_per_hour):
#         self.rent_per_hour = rent_per_hour

#     def Calculate_salary(self):
#         print(f"The rent per hour of a Contract Employee is: {self.rent_per_hour}")

# I = Intern(30_000)
# F = FullTimeEmoloyee(60_000)
# C = ContractEmployee(250)

# I.Calculate_salary()

'''
# __init__ is needed when:
# 1. The class must store some data (attributes) inside the object.
#    Example: name, age, salary, stipend, engine size, etc.
# 2. You want to pass values while creating the object.
#    Example: Intern(30000), Car("Tata", "Safari", 5)
# 3. Object needs initial setup before using it.
#
# In short:
# If your object needs to REMEMBER any value → __init__() is mandatory.
'''

'''
# __init__ is NOT needed when:
# 1. The class does not need to store any attributes.
#    Example: animal makes a sound, shape prints something, etc.
# 2. You are not passing any values while creating the object.
#    Example: Lion(), Cow(), Shape()
# 3. The class only performs actions (methods) without storing data.
#
# In short:
# If your object does NOT store data → __init__() is optional.
'''

#Concept: Costrutor Overloading (with Default parameters)
'''Q7. Create a class person that allows the constructor to work with:
        name only
        name + age
        name + age + address
       As diect constructor oberloading (multiple constructor are not allowed but we have to use default parameters
       to simulate constructor overloading.)'''

# class Person():
#     def __init__(self, name, age =None, address=None):
#         self.name = name
#         self.age = age
#         self.address =address

#     def show_name(self):
#         print(f"person name: {self.name}")

#     def name_age(self):
#         print(f"Person name: {self.name}, and their age: {self.age}")

#     def name_age_address(self):
#         print(f"Person name: {self.name}, their age: {self.age},and their address:{self.address} ")

# P1 = Person("Lokesh", 20, "Siwan, Bihar(841235)")
# P1.show_name()
# P1.name_age()
# P1.name_age_address()

# constrctor overloading means hota hai main class me hi ek hi __init__ se parameter likh lo aur usme se default 
# parameters lga lo phir uske aage function likh kar bari bari se alga alga parameters ko print karo 
# agar tum soch rhe ho ki subclass se bhi ho skta tha lekin ye shi nhi hai tab ye constructor overloading nhi kahalyega
# tab wo inheritance kahlayea jo code tumne pahle hi likh chuke ho upar wale Questions me 

'''Concept: Instance & class Atributes
ceate a class player with :
a class variable player_count
instance variables name and level

Track how many players were ceated '''

# class Player():
#     player_count = 0
    
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level

#         Player.player_count += 1
    
#     def show(self):
#         print(f"Name of player: {self.name}, Level of player; {self.level}")

#     @classmethod
#     def show_count(cls):
#         print(f"Total players: {cls.player_count}")

# P1 = Player("Lokesh", 1)
# P2 = Player("Adarsh", 2)

# Player.show_count()
# P1.show()
# P2.show()

'''Concepts: Multiple inheritance
Q9. create the following classes : Herbivore, Carnivore, Omnivore with some attributes and methods.
then create a class Bear that inferts from all the above classes to showcase how multiple inheritance
works.'''

# class Herbivore():
#     def __init__(self, ):
#         self.

# class Carnivore():
#     def __init__(self, ):
#         self.

# class Omnivore():
#     def __init__(self, ):
#         self.

# class Bear(Herbivore, Carnivore, Omnivore):
#     def __init__(self, ):
#         self.
