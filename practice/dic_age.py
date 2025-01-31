people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22},
    {"name": "David", "age": 28}
]
def get_age(person):
    return person["age"]
sorted_people=sorted(people,key=get_age)
print(sorted_people)
