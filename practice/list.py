'''list=[1,2,3,4,5,6,7,8,9]
result=[]
for i in list:
    if i%2==0:
       result.append(i)
print(result)

list_new=[2,3,4,6,7]
del list_new[2]
print(list_new)

list_key=["yugesh","arun","harish"]
list_value=[1,2,3,4]
output={k:v for (k,v) in zip(list_key,list_value)}
print(output)
result=dict(zip(list_key,list_value))
print(result)'''
'''test_dict = {'gfg': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]} 
print("The original dictionary is : " + str(test_dict))
res = dict()
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])
print("the sorted dictionary :" + str(res)) '''

#negative index is counting positioing from the last
'''list=[1,2,3,4,5,6]
list[2:4]=[9,9]
print(list)

map={}'''
lst1=[3,1,7,2,9,2]
lst2=[9,5,6,1,0,3]
final=lst1+lst2
res=[]
for i in sorted(final):
    res=i
print(res)

