'''a = ['apple',12,3, 'banana']
res = ' '.join(a)
print(res)'''

'''d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}
d3=d1.copy()
for key, value in d2.items():
    d3[key] = value

print(d3)'''
list_key=["yugesh","arun","harish"]
list_value=[1,2,3]
dic_new={k:v for (k,v) in zip(list_key,list_value)}
print(dic_new)
list_new=list(zip(dic_new.keys(),dic_new.values()))
print(list_new)
print(type(list_new))


