
# Create Dictionary

student = {
    "Name" : "Shiv" ,
    "Age" : 23,
    "Course" : "B.Tech"
}

print(student)


# Access Dictionary Values

student2 = {
    "Name" : "Harshad" ,
    "Age" : 14,
    "Course" : "Cs"
}

print(student2["Name"])
print(student2["Age"])
print(student2["Course"])


# Add a new key - value

student3 = {
    "Name" : "Om" ,
    "Age" : 22,
}

student3["City"] = "Indore"

print(student3)


# Update a value

student4 = {
    "Name" : "Sankar" ,
    "Age" : 20,
    "Course" : "MBA"
}

student4["Age"] = 21

print(student4)


# Delete an Element

student5 = {
    "Name" : "Rudra" ,
    "Age" : 25,
    "Course" : "BBA"
}

del student5["Course"]

print(student5)


# Dictionaries Methods
# Key ()

student6 = {
    "Name" : "Shivay" ,
    "Age" : 26,
    "Course" : "BSC"
}

print(student6.keys())


# Values ()

student7 = {
    "Name" : "Shivay" ,
    "Age" : 26,
    "Course" : "BSC"
}

print(student7.values())


# items

student8 = {
    "Name" : "Shivay" ,
    "Age" : 26,
    "Course" : "BSC"
}

print(student8.items())


# get ()

student9 = {
    "Name" : "Shivay" ,
    "Age" : 26,
}

print(student9.get("Name"))

print(student9.get("Age"))


# Update

student10 = {
    "Name" : "Shivay" ,
    "Age" : 26,
    "Course" : "BSC"
}

student10.update({"Age":21 , "City":"Indore"})

print(student10)


# pop

student11 = {
    "Name" : "Shivay" ,
    "Age" : 26,
    "Course" : "BSC"
}

student11.pop("Age")

print(student11)


# clear 

student12 = {
    "Name" : "Shivay" ,
    "Age" : 26,
    "Course" : "BSC"
}
student12.clear()

print(student12)


# Loop Through Dictiobary

# Only Keys

student13 = {
    "Name" : "Pooja" ,
    "Age" : 26,
    "Course" : "M.Tech"
}

for key in student13 :
    print(key)
    

# keys + values

student14 = {
    "Name" : "Pooja" ,
    "Age" : 26,
    "Course" : "M.Tech"
}

for key , value in student14.items() :
    print(key , "=" , value)
    

# Check Key Exists

student15 = {
    "Name" : "Harshita" ,
    "Age" : 26,
    "Course" : "MSC"
}

key = input("Enter Key :")

if key in student15 :
    print("Key Found:" , key)
else:
    print("Key Not Found")


# Nested Dictionary

student16 = {
    "student17" : {
    "Name" : "Ishwar" ,
    "Age" : 21,
    "Course" : "B.Tech"
}, 
    "student18" : {
        "Name" : "Neha" ,
        "Age" : 20,
        "Course" : "B.Tech"
    }
}
    
print(student16)


# Access Nested Ditionary

student19 = {
    "student20" : {
    "Name" : "Ankit" ,
    "Age" : 26,
    "Course" : "B.Tech"
}, 
    "student21" : {
        "Name" : "Rakesh" ,
        "Age" : 26,
        "Course" : "B.Tech"
    }
}

print(student19["student20"]["Name"])

print(student19["student20"]["Age"])

print(student19["student21"]["Name"])

print(student19["student21"]["Age"])


# Update Nested Dictionary

student22 = {
    "student23" : {
    "Name" : "Chiku" ,
    "Age" : 26,
    "Course" : "B.Pharma"
}
}

student22["student23"]["Age"] = 27

print(student22)


# Dictionary Comprehension

numbers = { 1, 2, 3 ,4 , 5 }

square = {i : i * i for i in numbers}

print(square)





