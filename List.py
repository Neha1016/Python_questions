# Largest Element 

lst = [10, 25, 8, 4, 77]

largest = lst[0]

for i in lst :
    if i > largest:
        largest = i
        
print("Largest = ", largest )


# Smallest Element 

sml = [10, 25, 8, 4, 77]

smallest = sml[0]

for i in sml :
    if i < smallest :
        smallest = i 
        
print("Smallest = " , smallest)
        

# Second Largest 

lst = [10, 25, 8, 4, 77]

largest = max(lst)

lst.remove(largest)

second = max(lst)

print("Second Largest = " , second )


# Remove Duplicate 

r_d = [10, 25, 8, 4, 10 , 25 , 1, 1 , 2 , 2 ]

result = []

for i  in r_d:
    if i not in result :
        result.append(i)
        
print(result )


# Sort List 

s_l = [10, 25, 8, 4, 77]

s_l.sort()

print(s_l)



# Merge Two  Lists

m_r1 = [1, 2, 3 ]
m_r2 = [4, 5, 6 ]

result = m_r1 + m_r2

print(result )



# Find Common elements 

f_c1 = [ 1, 2, 3, 4 ]

f_c2 = [ 3 , 4, 2, 1]

for i in f_c1 :
    if i in f_c2:
        print (i )



# Rotate List 

r_l = [ 22, 33, 44, 55, 66 ]

n = 2 

result = r_l[n :] + r_l[: n ]

print(result )


# Count Frequency 

cf = [1, 2, 3, 4, 1 ,2 ,3 ,4  , 5, 6 ]

seen = []

for i in cf :
    if i not in seen :
        print(i , "=" , cf.count(i))
        seen.append(i)


# Sum of Elements 

sum = [10 , 20 , 30 , 50 , 60 ]

total = 0 

for i in sum :
    total +=1 
    
print("Sum = " , total )


# Average Of List 

list = [10,20,30,40,50]

total = 0 

for i in list :
    total += i
    
average = total/len(list)

print("Average = " , average )


# Maximum And Minimum

max_min = [10,20,30,40,50]

print("Maximum =" , max(max_min))
print("Minimum =" , min(max_min))

# Reverse List 

list_reverse = [1,2,3,4,5]

print(list_reverse[::-1])

# Even or Odd Number In List 

even_odd = [ 10 , 20 , 40 , 43 , 33 ]

print("Even Numbers :")
for i in even_odd:
    if i % 2 == 0 :
        print(i)
        
print("Odd Numbers :")
for i in even_odd:
    if i % 2 != 0:
        print(i)