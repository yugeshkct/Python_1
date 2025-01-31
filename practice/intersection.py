lst1=['a','e','i','o','u']
lst2=[3,4,5,6,7,8]
d={}
for i in range(len(lst1)):
    d[lst1[i]]=lst2[i]
print(d)
'''def intersection(lst1,lst2):
    result=[]
    for item in lst1:
        if item in lst2 and  item not in result:
            result.append(item)
    return result

output=intersection(lst1,lst2)
print(output)'''

