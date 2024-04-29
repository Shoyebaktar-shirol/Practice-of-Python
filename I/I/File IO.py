
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



import os


os.remove("sample.txt")