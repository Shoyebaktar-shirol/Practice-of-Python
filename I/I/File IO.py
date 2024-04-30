
# Notes

# r     is use to read the data 
# w     use to write the Data
# a     is used for both reading and writing
# r+    read + overide (pointer start) no truncate 
# w+    read + overide (pointer end)  truncate 
# a+    read + append (pointer end) no  truncate   






# f = open("shoyeb.txt","r")
# data = f.read() #reads the entire data or txt
# print(data)
# f.close()


# f = open("shoyeb.txt","r")
# line1 = f.readline()#use to read the lines one by one entire line 
# print(line1)


# line2 = f.readline()#use to read the lines one by one entire line 
# print(line2)

# line3 = f.readline()#use to read the lines one by one entire line 
# print(line3)
# f.close()



# f = open("shoyeb.txt","w")
# f.write("i want to learn Data Structurs")# Deletes teh data from the previus data then adds the new data in file
# f.close()

# f = open("shoyeb.txt","a")
# f.write(" \nHello World")  # appends the data at the end  of file
# f.close()

# f = open("shoyeb.txt","r+")# it append data at the start point(overides data)
# f.write("Hello")
# f.colse()


# f = open("shoyeb.txt", "w+")  # Truncates the data and writes new data in that file
# f.write("Hello, I am Shoyeb Aktar Shirol. Currently, I am learning coding with Apna College.")
# f.close()


# f = open("shoyeb.txt", "a+")#
# f.write("Python.")
# f.close()


#DELETING THE FILE
# import os


# os.remove("sample.txt")


# with open("new.txt","w") as f:
#     f.write("Hii Everyone \n we are learnig \n Python\n from the apna college\n coding for DSA")
#     f.write("T master The programming  world ")



# with open("new.txt","r") as f:
#     data = f.read()
# new_data =  data.replace("Java","Python")
# print(new_data)


# with open("new.txt","r") as f:
#     f.write(new_data)







count = 0
with open("new.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) %2==0):
            count +=1
        

print(count)