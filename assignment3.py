persons = [
    {
        'name': 'Max',
        'age': 29,
        'hobbies': ['singing', 'dancing', 'painting']
    },
    {
        'name': 'Paddy',
        'age': 29,
        'hobbies': ['tennis', 'dancing', 'skiing']
    },
    {
        'name': 'Reyansh',
        'age': 7,
        'hobbies': ['kayaking', 'dancing', 'hiking']
    },
    {
        'name': 'Susha',
        'age': 29,
        'hobbies': ['cooking', 'baking', 'exercise']
    },
    {
        'name': 'Manuel',
        'age': 29,
        'hobbies': ['editing', 'movies', 'cycling']
    },
]

# 1
names = [el['name'] for el in persons]
print(names)

# 2
all_older_than_20 = all([el['age'] > 20 for el in persons])
print(all_older_than_20)

# 3
new_persons_list = [person.copy() for person in persons]
new_persons_list[0]['name'] = 'Anna'
print(persons)
print(new_persons_list)


# name, age, hobbies = persons[0]
# print(persons[0][name], persons[0][age], persons[0][hobbies])
p1, p2, p3, p4, p5 = persons
print(p1)
print(p2)
print(p3)
