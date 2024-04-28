# def cal(a,b):
#     sum = a+b
#     print(sum)
# cal(11,11)
# cal(41,11)
# cal(141,11)

# def cal(a,b,c):
#     sum = a+b+c
#     avg = sum /3
#     print(avg)
#     return avg

# cal(20,40,60)


# def cal_prod(a,b):
#     print(a*b)
#     return a+b

# cal_prod(20,30)


# def prod(a = 2 , b=10):
#         print(a*b)
#         return a+b

# prod()
  


# cities = [1,2,3,4,5,6,7,8]

# def print_len(list):
#    print(len(list))

# print_len(cities)

# n = 5
# def calculate_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i
#     print(fact)

# calculate_fact(6)


# def converter(usd_val):
#     inr_val = usd_val*83
#     print(usd_val,"USD=",inr_val,"INR")

# converter(2)

# n = int(input("Enter The Number :"))
# def Even_odd(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")

# Even_odd(n)



# Recursion
# def show(n):
#     if(n == 0):  # BASE CASE IMPORTANT
#         return 
    
#     print(n)
#     show(n-1)
# show(100)

# Recursion using factorial
# def show(n):
#     if(n==0):
#         return

#     print(n)
#     show(n-1)

# show(5)


# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return fact(n-1) * n

# print(fact(5))

# def cal_sum(n):
#     if n ==0:
#         return 0
#     return cal_sum(n-1) + n

# sum = cal_sum(10)
# print(sum)


def print_list(lst, ind=0):
    if ind == len(lst):
       return

    print(lst[ind])
    print_list(lst, ind + 1)

fruits = ["Banana", "Apple", "Mango", "Grapes", "Pineapple"]
print_list(fruits)
