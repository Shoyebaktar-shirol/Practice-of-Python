# # i = 1
# # while(i <= 5):
# #     print("Hello World")
# #     i += 1
# # print(i)


# # Practice of loops 
# # i=0
# # while(i<=):
# #     print(i)
# #     i +=1
  

# # i = 100
# # while i >= 1:
# #     print(i)
# #     i -= 1

# # n = int(input("Enter The Number To Multiply:"))
# # i = 1
# # while i <= 10:
# #     print(n * i)
# #     i += 1 
# # print(i)


# # n = [1,4,9,16,25,36,49,64,81,100]
# # idx = 0
# # while(idx < len(n)):
# #     print(n[idx])
# #     idx += 1


# #Finding the x element in the tuple
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 55
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#         print("Element Found At The Index Of:", i)
#         break
#     i += 1
# else:
#     print("The Element You are Searching for the element was Not Found in the Tuple, Please Enter a Valid Number.",x)




# def reverse_list(s):
#     return s[::-1]
# my_list = [1, 2, 3, 4, 5]
# result = reverse_list(my_list)
# print("Reversed list:", result)
# max_value = max(result)
# print("Maximum element in the reversed list:", max_value)
# print(result[1])




#Swapping of two numbers
# a = 0
# b = 10
# temp = a
# a = b
# b = a 
# print(a)  #op 10
# print(b)  #op 0

# def example(number):
#     if number % 2 != 0:
#         print("Odd Number")
#     else:
#         print("Even Number")
# example(6)  
# example(7)



# FACTORIAL OF NUMBER
# user = int(input("Enter The Number To Get The Factorial of:"))
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# user  = fact(user)
# print("Factorial of given Number is :", user)



# Check palindrome or Not

# def is_palindrome(string):
#     return string == string[::-1]
# string =input("Ente the string to check the palindrome ot not:")
# if is_palindrome(string):
#     print("Is Palindrome")
# else:
#     print("Not A Palindrome")

