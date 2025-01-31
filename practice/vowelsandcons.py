n="this is chiefNet"
vowels="aeiouAEIOU"
count=0
d=[]
for i in n:
    if i in vowels:
        count +=1 
    elif i not in vowels:
        d.append(i)
print(d)
print (count)