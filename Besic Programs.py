# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# print("After Swapping:", a)
# print("After Swapping:", b)   # Swapping of two Nums


# Swapping the values without using a third variable
# a = 10
# b = 30
# a = a + b
# b = a - b
# a = a - b
# print("After Swapping:", a)
# print("After Swapping:", b)


# Even And Odd Program 
# def number(n):
#     if n % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")
# number(26)



# Factorial of a Num
# def factorial(n):
#     if n==0 or n==1:
#         return(1)
#     else:
#         return(n*factorial(n-1))


# print(factorial(6))



#PALINDROM OR NOT

# def palindrome(string):
#     return string[::-1]


# string = input("Enter the String Please:")
# if palindrome(string):   # evaluates the true always  because it returns reversed string.
#     print("Yes it is Palindrome string")
# else:
#     print("It is not a palindrome string")




#FIBONOCCI SERIES 
# def fibonacci(n):
#     series = [0, 1]
#     while len(series) < n:
#         series.append(series[-1] + series[-2])
#     return series

# number = int(input("Enter the Number of Fibonacci terms: "))
# result = fibonacci(number)
# print("Fibonacci Series is :", result)





# LEAP YEAR OR NOT PROGRAM
def leapYear(year):   # it contain an additional day, February 29th 
    if year %4==0 and year%100!=0 or year %4==0: # mendatory both
        return True
    else:
        return False

year = input("Please Enter The Year :")
if leapYear(int(year)):
    print("Leap Year")
else:
    print("Not A leap Year")


    # Sum Of The DIGITS