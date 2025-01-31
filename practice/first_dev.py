# Lists of developers
list1 = [
    {"firstName": 'Mark', "lastName": 'G.', "country": 'Scotland', "continent": 'Europe', "age": 22, "language": 'JavaScript'},
    {"firstName": 'Victoria', "lastName": 'T.', "country": 'Puerto Rico', "continent": 'Americas', "age": 30, "language": 'Python'},
    {"firstName": 'Emma', "lastName": 'B.', "country": 'Norway', "continent": 'Europe', "age": 19, "language": 'Clojure'}
]

list2 = [
    {"first_name": "Kseniya", "last_name": "T.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript"},
    {"first_name": "Amar", "last_name": "V.", "country": "Bosnia and Herzegovina", "continent": "Europe", "age": 32, "language": "Ruby"}
] 
developer=list1+list2
index=0
while index<len(developer):
    dev=developer[index]
    print(index)
    if('language'in dev)and (dev['language']=='Python'):
        print(dev)
        break
    index=index+1
        
