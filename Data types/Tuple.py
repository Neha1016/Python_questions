# Tuple Operations 

t = (22,33,44,55,66,77)

print("Tuple:", t)
print("First Element:",t[0])
print("Last Element:",t[-1])
print("Length:",len(t))
print("Slicing:",t[0:4])
print("Count:",t.count(22))
print("Index:",t.index(44))
print("22 in tuple:", 22 in t)

# Tuple Concatenation 

t1 = (10, 20, 30 , 40 ,50 ,60 )
t2 = (70, 80, 90, 100 )

result = t1 + t2

print(result)

# Tuple Repetion 

t3 = (1,2,3)

print(t3*3)

# Tuple Packing (Menas Multiple value store in one tuple )

t4 = (10, 20 ,30 ,40 )

print(t4)

# Tuple Unpacking (Tuple values separate using another variables)

t5 = (10,20,30)

a,b,c = t5

print(a)
print(b)
print(c)

# Packing and Unpacking Together

student = "Shiv" , 20 , "B.Tech"

name ,age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)


# Unpacking Using * 

t6 = (1 ,2 , 3, 10 ,20 , 30 , 4, 5, 6)

a, *b , c = t6

print("a =", a)
print("b = ", b)
print("c = " ,c)