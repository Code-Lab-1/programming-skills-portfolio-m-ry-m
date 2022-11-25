#Change value of a key in a nested dictionary
dict = {
    'emp1': {'name': 'Emma', 'salary': 8500},
    'emp2': {'name': 'Norman', 'salary': 9000},
    'emp3': {'name': 'Ray', 'salary': 7500}
}

dict['emp3']['salary'] = 8500
print(dict)