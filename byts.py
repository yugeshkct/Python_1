even=[2,4,6,8,10]
arr=bytes(even)
print(arr)
#list comprehension
output=[i for i in even if i%2==0]
print(output)
#Set comprehension
input={1,2,3,4,5,6,7,8,9,10,11,12}
out={i for i in input if i%2==0}
print("set comprehension",out)
#dict
#dic
#out_dict={i:j for i,j in dict if  }
#print("dict_output",out_dic)
keys =['a','b','c','d','e']
values=[1,2,3,4,5]
my_dict={k:v for (k,v) in zip(keys,values)}
print(my_dict)
#DICT COMP
new_dict={x: x**3 for x in range(10) if x**3%4==0}
print(new_dict)
#nested dict
dict={k1: {k2: k1*k2 for k2 in range(1,7)} for k1 in range(1,3)}
print("result",dict)
###age using dict
original={'jack':23,"dharshan":93,"gowthan":30,"wikki":39}
new_dict={k:('old' if v>50 else 'young')
          for(k,v) in original.items()}
print(new_dict)
#dict
weekly={day:temp for(day,temp) in zip(day,temp_C)}
print(weekly)


