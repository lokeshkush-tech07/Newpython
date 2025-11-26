#print("why you are not fixing my problem")
#print("yess problem has fixed now")
#Write a program that takes in 2 numbers (&) and print the average.
'''
a= int(input("Enter your first number: "))
b= int(input("Enter your first number: "))

avg=(a+b)/2
print("Average of these two numbers is:", avg,  ".")
'''
#print("All are being fine")

# d = {
#     "name":"Lokesh", 
#     "studying":"B.sc", 
#     "cgpa":"7.45"
# }
#print(d)

# for key,value in d.items():
#     print(key, value)
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d.get("cgpa2"))
# new_items = {"locatin":"Siwan"}
# print(d.update(new_items))

# print(d)

# my_set = {1, 1, 4, 8, 2, 2, 6, 4, 4}

# print(my_set)
# print(type(my_set))
# print(len(my_set))

# s = {10, 20, 30}

# s.add(40)
# print(s)

# s.remove(10)
# print(s)

# print(s.pop())

# s.clear()
# print(s)


#union and intersection 

# A = {1, 3, 4, 2, 7, 5, 5}
# B = {2, 4, 7, 9, 2, 1, 4}

# print(A.union(B))
# print(A.intersection(B))

class Student:

    # -------------------------------------------------------
    # Constructor (init)
    # Yaha hum VALUES ko setter ke through set kar rahe hain
    # Taaki validation automatically apply ho jaye.
    # -------------------------------------------------------
    def __init__(self, name, roll_no, marks):
        self.name = name         # calls setter → validates → stores as private
        self.roll_no = roll_no   # calls setter
        self.marks = marks       # calls setter


    # =======================================================
    #                 NAME  (GETTER + SETTER)
    # =======================================================

    @property
    def name(self):
        # Getter: ye private variable ko return karta hai
        return self.__name       # private attribute

    @name.setter
    def name(self, value):
        # Setter: validation + private store
        if value.strip() == "":
            raise ValueError("Name cannot be empty")

        self.__name = value      # private variable set


    # =======================================================
    #             ROLL NUMBER (GETTER + SETTER)
    # =======================================================

    @property
    def roll_no(self):
        return self.__roll_no

    @roll_no.setter
    def roll_no(self, value):
        # Validation: must be between 1 and 100
        if not (1 <= value <= 100):
            raise ValueError("Roll number must be between 1 and 100")

        self.__roll_no = value


    # =======================================================
    #                MARKS (GETTER + SETTER)
    # =======================================================

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            raise ValueError("Marks cannot be negative")

        self.__marks = value


# -------------------------------------------------------
#               TESTING THE CLASS
# -------------------------------------------------------

s = Student("Lokesh", 12, 85)

print("Name:", s.name)
print("Roll No:", s.roll_no)
print("Marks:", s.marks)

# s.marks = -10  # This will raise error (testing validation)
