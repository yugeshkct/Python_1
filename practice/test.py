a=int(input("enter value"))
b=input("enter the String")
out={b:a}
print(out)
c=int(input("enter value"))
d=input("enter the String")
out.update({d:c})
print(out)
key=['a','b','c','d','e']
value=[1,2,3,4,5,6,7,8]
result={}
output={k:v for (k,v) in zip(key,value)}
print(output)
for i in range(len(key)):
    if key[i] not in result:
        result[key[i]]=value[i]
print(result)
