# i = 1 
# while i <= 100:
#     print(i)
#     i+=1


# i = 1
# while i >=1:
#     print(i)
#     i -=1

# n = int(input("ENter The Number To Multiply :"))
# i = 1
# while i<=10:
#     print(n*i)
#     i +=1



#Leanear Search
# numbers = (1,4,9,16,25,36,49,64,81,100)
# target = 100
# i = 0
# while i<len(numbers):
#     if numbers[i] == target:
#         print("Element Found At Index :",i)
#         break
#     i+=1



# list = [ 1,2,3,4,5,6,7,8,9]
# for x in list:
#     print(x)


# str = "abc","Bca","cool","D","E"
# for char in str:
#     print(len(char))
 


# list = (1,2,34,5,5,6,7,77,8,8,9,)
# for x in list :
#     if(x == 2):
#         print("Found At :",x)
#         break
#     print(x)

# seq = range(10)
# for x in seq:
#     print(x)


# for x in range(2,10,2):
#         print(x)  # range(start , stop , step)
        #output is 2,4,6,8



# for x in range(2,12,2):
#     print(x)
# for x in range(1,12,2):
#     print(x)


# for x in range(100,0,-1):
#     print(x)

# n = int(input("Enter The Number To Multiply:"))
# for x in range(1,11):
#     print(n*x)


n = int(input("Ente The Number To Get The Factorial :"))
factorial = 1
for i in range(1,n+1):
    factorial *=i
    i+=1
    print("The Factorial Number Is =",factorial)