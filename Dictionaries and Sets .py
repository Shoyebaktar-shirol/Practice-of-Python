# dict = {
#     "Name": "Shoyebaktar",
#     "sgpa": 8.92,
#     "Country": "India",
#     "Subjects": {
#         "Cyber": 99,
#         "Python": 98,
#         "Multimedia Animation": 92,
#         "Daa": 98,
#         "R Programming": 95
#     }
# }

# Printing all the keys in dictionary
# print(dict.keys())

# # Printing all the values in dictionary
# print(dict.values())

# # Printing key-value pairs of dictionary all
# print(dict.items())

# # Adding new Key
# dict.update({"Age": 17, "City": "Delhi"})
# print(dict)
# Updating value of existing key


#Sets in python sets items are unique and elements are immutable  stores the unorder pair of elements set ignores the duplicate value
# collection = {1,2,3,4,4,3,2,  "Hello", " Python"}# cannot print the duplicate values 
# print(collection)
# print(type(collection))
# print(len(collection))
 
# a = set() # Empty set 
# print(a)




#   SET METHODS
collection = ["Hello", "Python", "Java", "C programming"]  
print(collection.pop(0))  # Remove and return the element at index 0
print(collection)  # Print the modified list

a = {1,2,3,4,5,5}
b = {3,4,5,7,8,1}
print(a.union(b))# returns union of two sets i.e., {"1","2","3","4","5","   

x= {1,2,3,4,5,5}
y= {3,4,5,7,8,1}
print(x.intersection(y))# Returns common elements from both sets i.e.,{"3","4","5"}


# Practice Questions

# dict = {
#     "Cat":"A Small Animal",
#     "table":["A Peace of Furniture","List of facts and figures"]#\
# }
# print(dict)

# a  = {"Python","Java","C++","Python","JavaScript","Java","Python","Java","C++","C"}
# print(len(a))




empty_dict = {}
x = int(input("Enter Python Marks:"))
empty_dict.update({"Python":x})
x = int(input("Enter Java Marks:"))
empty_dict.update({"Java":x})
x = int(input("Enter C Programming Marks:"))
empty_dict.update({"C Programming":x})
print(empty_dict)
print("Highest Marks Obtained In :",max(empty_dict))
print(len(empty_dict))