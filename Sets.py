# Create a Set

s = {10 , 20 , 30 , 40 , 50}

print(s)


# Set Union 

s1 = {1, 2, 3}
s2 = {4, 5, 6}

print(s1.union(s2))
print(s1 | s2)


# Set Intersection 

s3 = {2, 3, 4 , 6}
s4 = { 1, 2, 5 , 6}

print(s3.intersection(s4))
print(s3 & s4)


# Set Difference

s5 = {1, 2, 3, 4}
s6 = {5, 6, 7, 8}

print(s5.difference(s6))
print(s5 - s6)


# Set Methods add()

s7 = {22, 33, 44, 55}

s7.add(66)

print(s7)


# remove ()

s8 = {22, 33, 44, 55}

s8.remove(55)

print(s8)


# discard 

s9 = {22, 33, 44, 55}

s9.discard(44)
s9.discard(77)    # if element not present it will not give an error

print(s9)


# POP

s10 = {22, 33, 44, 55}

a = s10.pop()      # remove one element form set 

print("Removed:" , a)
print("Set:", s10)       # Set is unordered that's why we can not say that which element will be remove 


# Clear  (Remove all elements)

s11 = {22, 33, 44, 55}

s11.clear()    

print(s11)


# Update set

s12 = {45, 46, 47}

s12.update([48 , 49 , 50])

print(s12)


# Symmetric Difference

s13 = {1, 2, 4, 5}
s14 = {4, 5, 6, 7}

print(s13.symmetric_difference(s14))
print(s13 ^ s14)


# Check Element Exists

s15 = { 10, 20, 30, 40, 50}

b = int(input("Enter element:"))

if b in s15:
    print("Element found:")
else:
    print("Element not found:")