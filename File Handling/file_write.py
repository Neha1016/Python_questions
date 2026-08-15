# Open the file in write mode

#'w' mode is used to write data into a file

# if the file already exists, old data will be overwritten

file = open("output.txt","w")

# write is used to write data into the file 
file.write("Hello Python")

# close () is used to close the file 
file.close()




# Write Multiple Lines

file = open("output.txt", "w")

file.write("Python\n")
file.write("C++\n")
file.write("Scala\n")

file.close()

print("Data Written Successfully")


# Write User Input to File 

name = input("Enter your name:")
age = input("Enter your age:")

file = open("output.txt", "w")

file.write("Name:" + name +"\n")
file.write("Age:" + age)

file.close()

print("Student Data Saved")




