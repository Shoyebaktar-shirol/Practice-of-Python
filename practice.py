# dict_ = {
#     "Name": "Shoyebaktar Shirol",
#     "Age": 22,
#     "College": "KLE SOCIETYS COLLEGE OF BCA GOKAK",
#     "Address": "Gokak",
#     "Degree": "BCA",
#     "CGPA": 8.62,
#     "Email": "shoyebaktarshirol@gmail.com",
#     "Phone": 9380373103
# }

# # Accessing keys of the dictionary
# keys = dict_.keys()
# print("Keys:", keys)

# # Printing the dictionary
# print(dict_)


# dicti = {"Name":"Shoyebaktar ",
# "Subjects":["DAA","Python","Java","Data Structures"],
# "Age":77,
# "Core_Subjects":("Networks","Operating Systems","Database Management System")
# }
# dicti["Age"] = 33
# print(dicti)


# Nested dictionary
# student = {
#     "Name ":"Shoyebaktar",
#     "College":"KLE BCA GOKAK",
#     "Subjects":{
#         "Java":99,
#         "Python ":98,
#         "DBMS":99
#     }
# }
# print(student["Subjects"])



# dict_ = {
#     "Name": "Shoyebaktar Shirol",
#     "Age": 22,
#     "College": "KLE SOCIETYS COLLEGE OF BCA GOKAK",
#     "Address": "Gokak",
#     "Degree": "BCA",
#     "CGPA": 8.62,
#     "Email": "shoyebaktarshirol@gmail.com",
#     "Phone": 9380373103
# }

# print(list(dict_.items())) # Type casted
# print(dict_.get("Name")) # use to get the value  of a key
# print(dict_.update({"City":"Gokak"}))
# print(dict_)





#SETS IN PYTHON

# a  = set()
# a.add(1)
# a.add(2)
# a.add(3)
# a.add(4)
# a.add(5)
# a.add("Shoyebaktar ")
# a.remove(2)
# print(a.clear())
# print(a)


# collection = {1,2,3,45,578}
# print(len(collection))



# a  = {1,2,3,4,5}
# b = {4,5,3,7,8,9}
# print(a.union(b))


# a  = {1,2,3,4,5}
# b = {4,5,3,7,8, 5,1,2,9}
# print(a.intersection(b))


# PRACTICE QUESTIONS

# student = {
#     "cat": "A small Animal",
#     "table": ["Table", "a piece of furniture", "list of facts and figures",]
# }
# print(student)



# subjects = {"python" , "java","c++","Python","Javascript","Java","python","java","c++","c"}
# print(subjects)
# print(len(subjects))

# student = {}
# sub1 = int(input("Enter The Marks Of Pyhton  :"))
# student.update({"Python":sub1})
# sub2 = int(input("Enter The Marks Of Java :"))
# student.update({"Java":sub2})
# sub3 = int(input("Enter The Marks Of C++  :"))
# student.update({"C++":sub3})
# print(student)


# number = input("Enter The Number: ")
# result= number[::-1]
# print(result)


# def practice(num1,num2):
#     result = num1 * num2
#     if result <=1000:
#         return result
#     else:
#         return num1+num2
    
# print(practice(77,30))


# user = input("")

# size = len(user)

# for i in range(0,size-1,2):
#     print(user[i],end=" ")



# user = input("")
# print(user[4:])
    
# def frist_last(number_list):
#     first = number_list[0]
#     last = number_list[-1]
#     if number_list[0] == number_list[-1]:
#         print(True)
#     else:
#         print(False)

# result = frist_last([1, 2, 3, 4, 4, 3])
# print(result)






# def frist_last(number_list):
#     first = number_list[0]
#     last = number_list[-1]

#     return first == last

# result = frist_last([1, 2, 3, 4, 4, 1])
# print(result)

# i = 0
# a = [10, 20, 33, 40, 55, 43]

# while i < len(a):
#     if a[i] % 5 == 0:
#         print(a[i])
#     i += 1


# a = [10, 20, 33, 40, 55, 43]
# for num in a:
#     if num%5==0:
#         print(num)



# str_x = "Emma is good developer. Emma is a writer"
# print(str_x.count("Emma"))




# for num in range(10):
#     for i in range(num):
#         print(num,end=" ") #print number
   
#     print("\n")



# def merge_list(list1,list2):
#         result_list = []
#         for num in list1:
#             if num%2!=0:
#                 result_list.append(num)


#         for num in list2:
#             if num%2==0:
#                 result_list.append(num)

#         return result_list

# list1= [1,2,3,4,5,6,7,8,9]
# list2 = [10,20,30,40,50,55,66,77]
# result = (merge_list(list1,list2))
# print(result)




# def reverse_int(number):
#     return number[::-1]




# user = int(input())
# if reverse_int(user):
#     print(number)
# else:
#     print("Finding")



# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end=" ")
#     print("\t")




# a = "shoyebaktar"
# print("".join(a))


# b = "S  H  O  Y  E  B  A  K  T  A  R"
# result = b.replace("  "," ")
# print(result)




# i = 1
# user = int(input("Enter The Number :"))
# while i<=10:
#     print(user*i)
#     i+=1

# a = 27873.2222
# print('%.2f' % num)

# a = []
# for i in range(0,5):
#     print("Enter The number at the location",i, ":")
#     result = float(input("Enter The number:"))
#     a.append(result)
#     print(a)

# read test.txt
# with open("a.txt", "r") as fp:
#     # read all lines from a file
#     lines = fp.readlines()


# with open("b.txt", "w") as fp:
#     count = 0
   
#     for line in lines:
#         # skip 5th lines
#         if count == 4:
#             count += 1
#             continue
#         else:
         
#             fp.write(line)
    
#         count += 1

# str1, str2, str3 = input("Enter three string").split()
# print('Name1:', str1)
# print('Name2:', str2)
# print('Name3:', str3)
