# Reverse a string 

a = input("Enter a string :")
print(a[::-1])

# Palindrome String 

b = input("Enter a string :")

if b == b[::-1]:
    print("Palindrome")
else:
    print("Not palindrome ")
    
# Count Vowels

c = input("Enter a string :")
count = 0

for i in c :
    if i.lower() in "aeiou":
        count +=1 
        
print("Vowels:", count)

# Count words

d = input("Enter a string :")

words = d.split()

print("Total words:", len(words))

# Remove Spaces 

e =  input("Enter a string :")

result = e.replace(" ","")

print(result)

# Replace Character 


f = input("Enter a string :")

old = input("Enter character to replace :")

new = input("Enter new character  :")

result = f.replace(old,new)

print(result)

# Check Anagram


g1 = input("Enter first string :")

g2= input("Enter second string :")

if sorted (g1) ==sorted (g2):
    print("Anagram")   
else:
    print("Not Anagram")
    
# Find Duplicate Characters 


h = input("Enter a string :")
for i in h :
    if h.count(i)>1:
        print(i, end="")
        
        
# Frequency of Character 


j = input("Enter a string :")

for i in j :
    print(i , "=", j.count(i))
    
    
# Convert Uppercase to Lowercase


k = input("Enter a string :")

print(k.lower())



# Remove Duplicate character 

l = input("Enter a string :")

result = ""

for i in l :
    if i not in result :
        result += i

print(result )

# First Non - Repeating Character 


m = input("Enter a string :")

for i in m :
    if m.count(i)==1:
        print("First non - repeating character :" , i)
        break 
    

# Longest Word 

n = input("Enter a sentence :")

words = n.split()

longest = ""

for i in words :
    if len(i) > len(longest):
        longest = i
print("Longest word :", longest)


# Check Substring 

o = input("Enter main string  :")
o_sub= input("Enter substring  :")

if o_sub in o :
    print("substring found")
    
else:
    print("Substing not found ")
    
    
# String Compression

p = input("Enter a string  :")

result = ""
count = 1 

for i in range(len(p)-1):
    if p[i] == p[i + 1]:
        count +=1
    else:
        result += p[i] + str(count)
        count = 1
        
result += p[-1] + str (count)

print(result )


# Reverse Words 

q = input("Enter a sentence:")

words = q.split()

print(" ".join(words[::-1]))


# Remove Special Chracters

r = input("Enter a string  :")

result = ""

for i in r :
    if i.isalnum() or i == "":
        result += i
        
print(result)


# Capatalize First letter of each word

t = input("Enter a sentence  :")

print(t.title())


# ASCII values of characters 

u = input("Enter a string  :")

for i in u :
    print(i , "=", ord(i))
    
    
# String Rotation 

v = input("Enter a string  :")

w = int(input("Enter rotation  :"))

w = w % len(v)

result = v[w:] + v[:w]

print(result )



