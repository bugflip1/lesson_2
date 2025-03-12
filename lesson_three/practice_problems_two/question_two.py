numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8
number2 = 95

def find_if_number_in_list(given_list, number):
    return number in given_list

print(find_if_number_in_list(numbers, number1))
print(find_if_number_in_list(numbers, number2))