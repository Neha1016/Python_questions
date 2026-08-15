# List Operations 

l1 = [10, 20 , 30 , 40 , 50 ]

print("Original List :" , l1)

l1.append(60)
print("After Appened :" , l1)

l1.insert(6, 70)
print("After Insert :" , l1)

l1.remove(60)
print("After Remove :" , l1)

l1.pop()
print("After Pop :" , l1)

print("Length:" ,len(l1))


# Sorting List (Ascending)


l2 = [105, 201 , 305 , 408 , 50 ]

l2.sort()

print(l2)


# Sorting List (Desending)


l3 = [190, 240 , 430 , 540 , 650 ]

l3.sort(reverse = True )

print(l3)


# Search Element 

l4 = [10, 20 , 30 , 40 , 50 ]

m = int(input("Enter element to search:"))

if m in l4 :
    print("Element Found")
else:
    print("Element Not Found")


# Linear Search 


l5 = [10, 20 , 30 , 40 , 50 ]

n = int(input("Enter element :"))

for i in range(len(l5)):
    if l5[i] == n:
        print("Element found at index" , i)
        break 

else:
    print("Element Not Found")
    
    
# List Comprehension (Square)


l6 = [10, 20 , 30 , 40 , 50 ]

square = [i * i for i in l6]

print(square)


# List Comprehension (Even Numbers)


l7 = [10, 4 , 5 , 7 , 9 , 11, 12,  20 , 30 , 40 , 50 ]

even = [i for i in l7 if i % 2 == 0]

print(even)


# List Comprehension (Odd Numbers)


l8 = [10, 4 , 5 , 7 , 9 , 11, 12,  20 , 30 , 40 , 50 ]

odd = [i for i in l8 if i % 2 == 0]

print(odd)


# Reverse a list 


l9 = [10,  20 , 30 , 40 , 50 ]

print(l9[::-1])


# Remove Duplicates From List 

l10 = [10,  20 , 30 , 40 , 50 , 10 , 20 , 5 , 5 , 6 , 7 , 3 , 6]

result = []

for i in l10:
    if i not in result:
        result.append(i)
        
print(result)

# Find Maxinum and Minimum

l11 = [10,  20 , 30 , 40 , 50 ]

print("Maximum = ", max(l11))
print("Minimum = ", min(l11))

# Sum of List Element 

l12 = [10,  20 , 30 , 40 , 50 ]

total = 0 

for i in l12:
    total +=1 
    
print("Sum = ", total)







