
# Open file in read mode

# 'r' mode is used to read existing data from a file 

file = open("data.txt","r")

# read () reads the complete content of the file
data = file.read()

# Display the file content
print(data)

# Close the file after reading 
file.close()


# Read File Line By Line using loop

file = open("data.txt","r")

for line in file :
    print(line)

file.close()



# Read Only First Few Characters 

file = open("data.txt","r")

data = file.read(10)

print(data)

file.close()


# Read Only First Line

file = open("data.txt","r")

data = file.readline()

print(data)

file.close()

# Read ALL lines

file = open("data.txt","r")

data = file.readlines()

print(data)

file.close()


