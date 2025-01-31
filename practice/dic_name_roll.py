students={}
while True:
    name=input("enter the user name:")
    roll_num=int(input("enter the roll number:"))   
    students[name]=roll_num
    choice=input("if you want to continue:")
    if choice!="yes":
        break
print(students)
