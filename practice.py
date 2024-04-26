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


number = input("Enter The Number: ")
result= number[::-1]
print(result)
