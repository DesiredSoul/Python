names = ["ata","dylan","tom"] 
for i in range(0,6):
    try:
        print(names[i])
    except:
        print("There are no more names")

print("Program continuing")


age=""
while isinstance(age,str):
    try:
        age = int(input("Enter age:"))
    except:
        print("error")

print("success")