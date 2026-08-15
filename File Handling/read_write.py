 

with open("sample.txt", "w") as file :
    file.write("Hello God")
    file.write("\n File Handling")
    
print("Data Written")


with open("sample.txt", "r") as file :
    data = file.read()
    
print(data)


with open("sample.txt", "a") as file :
    file.write("\n New Data Added")
    
print("Data Appended")
    
    
