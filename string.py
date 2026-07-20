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