STARTER = 'The Flintstones Rock!'

def display_ten_times_with_hyphen(message):
    for num in range(1,11):
        print(('-' * num) + message)

display_ten_times_with_hyphen(STARTER)