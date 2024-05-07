# class Car:
#     color = "Red"
#     brand = "Audi"
#     price = 9000000

# obj = Car()
# print(obj.color)
# print(obj.brand)
# print(obj.price)


#CUNSTRUCTURE
# class Student:
#      name = "Sameer"
#      def __init__():
#         print("Creating New Student in Database")
    

# s1 = Student()
# print(s1.name)



# class student:
#         name = "Shoyebaktar Shirol"
#         college = "KLE BCA GOKAK"
#         color = "Red"
# obj = student()
# print(obj.name)
# print(obj.college)
# print(obj.color)

# class Cars:
#         color = "Blue"
#         brand = "Audi"
# car1 = Cars()
# print(car1.color)
# print(car1.brand)



# CUNSTRUCTOR  AND METHODS
# class Student:
   
#         college = "KLE BCA GOKAK"
#         Digree = "BCA"
#         Passout = 2024
#         def __init__(self, Fullname):
#                 self.name = Fullname
#                 print("Cunstructure will Get the Call Frist The The Object Properties are printed")

# obj = Student("john")
# print(obj.name)

#DEFAULT CUNSTRUCTOR And Self is keyword use it mendatory otherwise we get Error
# class Shoyeb:
#         def __init__(self):
#                 print("Hello I am Learning cunstructor in Oops\nA Cunstructor is automatically called when an object is created.")

# obj2 = Shoyeb()


#PARAMETERISED CUNSTRUCTOR
# class demo:
     
#         def __init__(self,lastName):
#                 self.name = lastName
#                 print("Cunstructor will called autometically when an object is created")
        
# obj1 = demo("JACK MA")
# print(obj1.name)

#Method and Class

# class Student :
#         collge = "KLE BCA GOKAK"

#         def __init__(self):
#                 self.name = name 
#                 self.lastname = lastName

#         def welcome(self):
#                 print("Hello Methods")
# s1 = Student("SHoyebaktar","shirol")
# s1.welcome()



# class Student:
#         def __init__(self,name,marks):
#             self.name = name 
#             self.marks = marks
        

#         @staticmethod  # There is no self parameter i static methd work at the class lavel
#         def show():
#                 print("Hello World")
#                 print("this is the static method ")


#         def get_avg(self):
#                 sum = 0
#                 for val in self.marks:
#                         sum += val
#                         print("Hi",self.name,"Ur  Avg Score is:",sum/3)

# s1 = Student("Tony",[95,87,65])
# s1.get_avg()
# s1.show()


# class demo:


#     @staticmethod
#     def hello():
#         print("This is a static method inside a class")
#         print("I created indide the class ")
#         print("Ststic method works for class level only")

# s1 = demo()

# demo.hello()  # Correct way to call the static method


#



