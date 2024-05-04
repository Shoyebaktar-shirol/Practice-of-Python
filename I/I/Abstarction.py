#Abstarction in OOPS
# class car:
#     def __init__(self):
#         self.accelarator = False
#         self.brk = False
#         self.cluch = False
#     def start(self):
#         self.accelarator =True
#         self.cluch = True
#         print("Car Is Started Now >...")

# car1 = car()
# car1.start()


# class account:
#     def __init__(self,bal,acc):
#        self.balance = bal
#        self.account_no = acc



# def debit(self,amount):
#     self.balance =- amount
#     print("Rs    amont the debit a")

# acc1 = account(10000,12345)
# print(acc1.balance)
# print(acc1.account_no)


#Abstraction is a  hiding the implementation details of the classs and showing only the essential information to the user
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True 
        self.clutch = True
        print("Car Started successfully")

car1 = Car()
car1.start() 
