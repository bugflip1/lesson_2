numbers = [1, 2, 3, 4]

def delete_list(given_list):
    given_list.clear()
    return given_list

def delete_list_two(given_list):
    del given_list[:]
    return given_list

print (delete_list(numbers))

print(delete_list_two(numbers))

