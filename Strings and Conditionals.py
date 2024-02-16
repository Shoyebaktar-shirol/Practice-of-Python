# str1 = "String is sequence of characters enclosed in the double quotes\n "
# str2 = "In Python String is a Immutable "
# print(str1+str2)#concatenation Two strings
# print(len(str1))#printing the length of string remember white space is also calculated for length


# str = "SHOYEBAKTAR_SHIROL"
# print(str[11]) #underscore also calculated as index position 


#Slicing in Python and Ending  Index is not included.
# str = "SHOYEBAKTAR"
# print(str[-3:-1])#from -1 to -5 means from last element to fifth last element 
#output will be TA


#String Functions
# str1  = "IamSHoyebaktar"
# print(str1.endswith("tar"))  #it returns the T or F Value

# str2 = "shoyebaktar"
# print(str2.startswith("sho"))#it returns the T or F Value

# cap = "shoyebaktar_shirol"
# print(cap.capitalize())    #It convert first character of each word into capital letter

# rep = "Bachelor of computer application from kle bca gokak"
# print(rep.replace("o","Z"))# It replace all o with Z

# rep2 = "I was interested in Full Stack Dev"
# print(rep2.replace("Dev","Development"))

# find = "I am Practicing Python"
# print(find.find("I"))
# it return starting index value if we provide substring which is present in string otherwise it returns -1



# count_function = "Learning from Apna College"
# print(count_function.count("g"))
#It count how many times 'G' comes in the given sentence
#output will be 2 


# Practice Quetions
# str  = (input("Enter Your Name Please :"))
# print("You have entered string is  :",str)
# print("The Length of the string is :",len(str))


# occurence = "I am Shoyebaktar_Shirol Persuing Bca from Gokak"
# print(occurence.count("a")) #output will be 5 




# COnditionals in Python if and else 
# age = 18
# if(age >= 18):
#     {
#  print("Eligible for voting and u can apply for licence")
#     }
# else:
#     {
#         print("Sorry U are not eligible for applying the licence")
#     }



    # if and elif
# light = "Green"
# if (light == "red"):
#     print("Stop Signal")
# elif (light == "yellow"):
#     print("Slow Down")
# elif (light == "Green"):
#     print("Cross the road carfully")
#     print("Safe Journey")


#practice code
# name = input("Enter your name: ")
# marks = int(input("Enter your marks to check the grade: "))
# if marks >= 90:
#     grade = "A"
#     print("Congratulations,", name, "!")
#     print("You've scored Grade A. You are the topper of the class!")
# elif marks >= 80:
#     grade = "B"
#     print("Congratulations,", name, "!")
#     print("You've scored Grade B.")
# elif marks >= 70:
#     grade = "C"
#     print("Congratulations,", name, "!")
#     print("You've scored Grade C.")
# elif marks >= 60:
#     grade = "D"
#     print("Congratulations,", name, "!")
#     print("You've scored Grade D.")
# elif marks >= 50:
#     grade = "E"
#     print("Congratulations,", name, "!")
#     print("You've scored Grade E.")
# else:
#     grade = "Fail"
#     print("Sorry,", name, "!")
#     print("You've failed. Try better next time.")

# print("Candidate Name:", name)
# print("Grade:", grade)



#Practice Questions Even or Odd Number Check
# user = int(input("Enter The Number :"))
# if user % 2==0:
#     print("EVEN NUMBER")
# else:
#     print("ODD NUMBER")


#Practice Questions Greatest among  three number Check
# a = int(input("Enter The Frist Number  :"))
# b = int(input("Enter The Second Number:"))
# c = int(input("Enter The  Third Number :"))
# if(a>=b and a>=c):
#     print("Frist Number Is The Larger",a)
# elif(b>=c):
#     print("Second Number Is The Larger",b)
# else:
#     print("Third Number Is The Larger")


#Check the multiple of 7 number or not 
a = int(input("Enter  Number  :"))
if(a%7==0):
    print("Multiple of 7 Number")
else:
    print("Not multiple of 7 Number")

