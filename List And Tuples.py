# Lists Are Mutable In Python

# List = [90.3,44.6,88.8,97.8,55.6,96.8]   
# print(List)
# print(type(List))
# print(len(list))
# print(List[0])

# l = ["Shoyebaktar", 20, "Gokak"]
# print(l)
# l[0] = "Shoyebaktar Shirol"# We Can Change The Value Of Element At Given Index
# print(l)

#Slicing in List
# a = [2,3,4,5,6,7,8,9]
# print(a[0:5])

#negetive indexing of slicing
# l = [1,2,3,4,5,6,7,8,9]
# print(l[-8:-5])# Output: [5,6,7]

#List Methods
# list  = [1,2,3,4,5,6,7,8]
# list.append(9) # append() is used for add element at the End of The List
# print(list)#

# s = [23,4,5,6,66,77,88,99,33]
# print(s.sort())# sort() is used for Sorting The List
# print(s)

# r = [1,2,3,4,5,6,7,8,9]
# print(r.reverse()) # used for reverse the elements  of the list
# print(r)#Output : [9,8,7,6,5,4,3,2,1]

# I = [1,2,3,4,5,6,7,8,9]
# I.insert(0,10) # changes the element of index position  and insert the new value at that place 0 will be the index position
# print(I)#Output : [10, 1, 2, 3, 4, 5]


# P = [1,2,3,4,5,6]
# print(P)
# print(P.pop(1))# pop() is used to remove the element from the given index and return that value
# print(P)


#Tuples in Pyhton Tuple are  Immutable Like String In Python
# tup = (1,2,4,5,6,7,8,9)
# print(tup)
# print(type(tup))# output : <class 'tuple'>

# TUPLE METHODS|
# tup = (1,2,3,4,5,6,7,8,9)
# print(tup.index(4))# Index() is used To find the Element At Which Position We Want Is Present
# print(tup)#output : 3

# t = ("Shoyebaktar_Shirol")
# print(t.count("o")) #  count() is used For Count How Many Times A Character Is There In The List Or Tupple
# print(t)


# movies = []# Create an empty list called movies
# movie1 = input("Enter The Frist Movie Name:")
# movie2 = input("Enter The Second Movie Name:")
# movie3 = input("Enter The Third Movie Name :")
# movies.append(movie1)# append() is used to add The Value To The End Of The List
# movies.append(movie2)
# movies.append(movie3)
# print(movies)



#List contain palindrome or not 
# list1 = [1,2,1]
# list2 = [3,2,1]
# list1  = list1.copy()# This Is Used To Copy The List
# list1.reverse()# Reverse() Is Used To Reverse The List

# if(list1 == list1):# If Both Are Equal Then it is  Palindrome
#     print("Palindrome")
# else:
#     print("Not a Palindrome")



# Practice counting the Grade A how many time occuring
# grade = ["C","D","A","A","B","B","A"]
# print(grade.sort())
# print(grade)



#split()
# user = input("Enter A String:")
# user = user.split()  
# print(user)



n = int(input("Enter a number:"))
arr = list(map(int, input().split()))
product = 1
for num in arr:
    if num % 2 == 0:
        product *= num
print(product)

