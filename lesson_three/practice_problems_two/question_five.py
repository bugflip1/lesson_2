numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

def is_string(given_argument):
    return isinstance(given_argument, list)

print(is_string(numbers))
print(is_string(table))