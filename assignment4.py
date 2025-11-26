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

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name #private attribute
        self.__roll_no = roll_no #private attribute
        self.__marks = marks #private attribute

    def get_info(self): #function for getting information of indivisual students details
        print(f"Name: {self.__name}, Roll no: {self.__roll_no}, Marks: {self.__marks}")

#-----------------------------------------
# using getter method for indirectly acces
#-----------------------------------------

    def get_name(self): #for name
        return self.__name
    
    def get_roll_no(self): # for roll no
        return self.__roll_no
    
    def get_marks(self): # for marks
        return self.__marks
    
#-----------------------------------------
# Using setter method for modification
#-----------------------------------------
    def set_name(self, new_name): #name modificaion
        if new_name.strip() == "":
            print("Name cannot be empty !")
        else:
            self.__name = new_name

    def set_roll_no(self, new_roll_no): #Roll no modification
        if 1<= new_roll_no <= 100:
            self.__roll_no = new_roll_no
        else:
            print("Roll no has to must be btw 1 to 100")

    def set_marks(self, new_marks): # Marks Modification
        if new_marks < 0:
            print("Marks cannot be negative")
        else:
            self.__marks = new_marks

S1 = Student("Lokesh", 33, 358)
S1.get_info()
