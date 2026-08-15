
# Open the file in append mode

# 'a' mode adds new data at the end of the existing file

# Existing data is not deleted 

file = open("ss.txt", "a")

# Add new data to the file
file.write("\n This is new data.")
file.write("\n I am using append mode.")

file.close()

print("Data appended Successfully")


# Append User Input 

name = input("Enter your name:")
age = input("Enter your age:")

file = open("ss.txt", "a")

file.write("\n Name:" + name)
file.write("\n Age:" + age)

file.close()

print("Data added Successfully")