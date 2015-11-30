students = [
    {'name': 'Tibi', 'age': 8},
    {'name': 'Adorjan', 'age': 9},
    {'name': 'Agoston', 'age': 6},
    {'name': 'Aurel', 'age': 7},
    {'name': 'Dezso', 'age': 12}
]

students_at_least_8 = []

def students_at_least_8(list):
    filtered = []
    for n in list:
        if n['age'] >= 8:
            filtered.append(n)
    return filtered

def students_ages_starting_with_A(list):
    filtered = []
    for n in list:
        if n['name'][0] == 'A':
            filtered.append(n['age'])
    return filtered

students1 = students_at_least_8(students)
print(students1)
# > [{'age': 8, 'name': 'Tibi'}, {'age': 9, 'name': 'Adorjan'}, {'age': 12, 'name': 'Dezso'}]

students2 = students_ages_starting_with_A(students)
print(students2)
# > [9, 6, 7]
