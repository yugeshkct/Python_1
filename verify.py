username="yugesh"
pwd="123"
usr=input("enter the username:")
pwd1=input("enter the password:")
def validate():
    if(usr==username and pwd1==pwd):
        return True
    else:
        return False
a=validate()
print(a)

