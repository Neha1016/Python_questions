# Word Frequency 

word_freq = input("Enter a sentence :")

words = word_freq.split()

f = {}

for i in words:
    f[i] = words.count(i)
    
    print(f)


# Student Marks Dictionary 

marks = {
    "Shiv": 95,
    "Mahdev":96,
    "Shankar":97
    
}

for i in marks:
    print(i, "=" , marks[i] )
    
    
# Merge Dictionary 

d1 = {"a":1 , "b":2}
d2 = {"c":3, "d":4} 

d1.update(d2)

print(d1)


# Invert Dictionary 

in_dic = {"a":1 , "b":2 , "c":3, "d":4} 

new = {}

for i in in_dic:
    new[in_dic[i]] = i
    
print(new)


# Duplicate Value

dup_val = {"a":1 , "b":2 , "c":1, "d":4 , "e": 2} 

seen = []

for i in dup_val.values():
    if i not in seen:
        if list(dup_val.values()).count(i)>1:
            print(i)
        seen.append(i)
    
    
# Set Union

s1 = {1,2,3}
s2 = {4,5,6}


print(s1 | s2)

