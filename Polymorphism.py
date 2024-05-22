
#polymorphism when the same operator allowed ti have diffrent meaning according to the context .abs

# class complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img


#     def showNum(self):
#         print(self.real,"i +",self.img,"j")


# num1 = complex(1,3)
# num1.showNum()
    



# class circle:
#     def __init__(self,radius):
#         self.radius = radius


#     def area(self):
#         return 3.14 * self.radius ** 2



#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# c1 = circle(21)
# print(c1.radius())
# print(c1.area())




class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)


class Engineer(Employee):
    def __init__(self, name, age, salary):
        super().__init__("Engineer", "IT", salary)
        self.name = name
        self.age = age


eng1 = Engineer("Elon Musk", 40, 1000000)
eng1.showDetails()



print("EMPLOYEE DETAILS")


e1 = Employee("Shoyebaktar Shirol","Finance","90000")
e1.showDetails()

