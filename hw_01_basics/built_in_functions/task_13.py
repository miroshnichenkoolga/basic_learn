people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob',   'age': 25},
    {'name': 'Carol', 'age': 35}
]

def sort_people_by_age(people):
    return sorted(people, key=lambda person: person["age"])


print(sort_people_by_age(people))
# [
#   {'name': 'Bob',   'age': 25},
#   {'name': 'Alice', 'age': 30},
#   {'name': 'Carol', 'age': 35}
# ]