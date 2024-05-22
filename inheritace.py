# # class car:
# #     @staticmethod
# #     def  start():
# #         print("Car is started now")

# #     @staticmethod
# #     def stop():
# #         print("CAr Is Stopped Now")



# # class audi(car):
# #     def __init__(self,name):
# #         self.name = name 

# # car1 = audi("Fortuner ")
# # car2 = audi("BMW")
# # print(car1.name)   # single inheritence 





# #MULTILEVEL INHERITENCE

# class car:
#     @staticmethod
#     def  start():
#         print("Car is started now")
#         print("Now u can ready to GO ...")

#     @staticmethod
#     def stop():
#         print("CAr Is Stopped Now")
#         print(" car is Stopped plese wait for while ...")


# class audi(car):
#     def __init__(self,brand):
#         self.brand = brand

# class fortuner(audi):
#     def __init__(self,type):
#         self.type = type   


# car1 = fortuner("Petrol")
# print(car1.start())








#MULTIPLE INHERITENCE 
#It inherits the multiple classes seperated by ,,,,

# class A:
#     carA = " Welcome to class A"

# class B:
#     carB = " Welcome to class B"

# class C:
#     carC = " Welcome to class C"

# class  D(A,B,C):
#     carD = " Welcome to class D"

# obj_for_D1 = D()
# print(obj_for_D1.carA)
# print(obj_for_D1.carB)
# print(obj_for_D1.carC)
# print(obj_for_D1.carD)   # above i am  inheriting A , B , C In deriver class D



#DECORATORS IN PYTHON 
#@instancemethod - we can acces both class and method 
# @classmethod   - cannot change or access the attributes
#@staticmethhod - can change or access the attributes
#@propertymethod - 


#EXAMPLE FOR @proprtymethod

class student:
    def __init__(self,java, C, Python):
        self.java = java
        self.C = C
        self.Python = Python
       
    @property
    def percentage(self):
        return (self.java + self.C + self.Python)/3 

stud1 = student(99,98,97)
print(stud1.percentage)


stud1.C = 77
print(stud1.percentage)