# IMPORTS #

# JSON import and setup
import json

with open('calculator/calculator.json', 'r') as file:
    data = json.load(file)
# Python debug
import sys

# FUNCTIONS #

def safeinput(message): # pylint: disable=unused-argument
    # Checks for keyboard interrupts during inputs
    try:
        return input(message)
    except KeyboardInterrupt:
        try:
            lan
        except NameError:
            print(data["english"]["ifinterrupt"])
        else:
            print(lan["ifinterrupt"])
        sys.exit(1)

def welcome(): # Welcome message
    print(prompt(data["english"]["welcome_messages"]))

def prompt(message): # Adds a arrow to the start of messages
    return f"==> {message}"

def languagegrabber(): # Language grabber
    message = prompt(
        f"{data["english"]["langrabber"]}"
        f"{lanstr(lanlister(data))}")
    language = safeinput(message).lower()
    return language

def lanlister(all_messages): # returns list of lan from json file
    return list(all_messages.keys())

def lanstr(lanlisted): # Makes the list of languages a string
    lanlisted = [ languages.title() for languages in lanlisted ]
    if len(lanlisted) >= 3:
        last = lanlisted.pop(-1)
        finallist = ", ".join(lanlisted)
        finallist += f", or {last}"
    else:
        finallist = " and ".join(lanlisted)
    return f"({finallist})\n"

def lancheck(user_input, lst): # Checks if user input is lan in json

    while user_input not in lst:
        print(prompt(data["english"]["invalidlan"]))
        user_input = languagegrabber()
    return user_input

def main(): # Main function
    # Ask the user for the first number
    number1 = safeinput(prompt(lan["numoneprompt"]))
    while not is_numeric(number1):
        number1 = safeinput(prompt(lan["invalidnum"]))

    # Ask the user for the second number
    number2 = safeinput(prompt(lan["numtwoprompt"]))
    while not is_numeric(number2):
        number2 = safeinput(prompt(lan["invalidnum"]))


    # Ask the user for the operation to perform
    operation = safeinput(prompt(lan["opprompt"]))

    # Perform the operation on the two numbers
    number1, number2 = conv_int(number1, number2)

    # Print the result to the terminal
    print(
        f'{lan["result"]} {operation_complete(number1, number2, operation)}'
        )

def is_numeric(s): # Is numeric function, really only checks for floats
    try:
        float(s)
        return True
    except ValueError:
        return False

def conv_int(num1, num2): # Converts the input to floats
    return float(num1), float(num2)

def operation_complete(num1, num2, op): # pylint: disable=unused-argument
    while op not in ('+', '-', '*', '/'):
        print(prompt(lan["invalidop"]))
        op = safeinput(prompt(lan["opprompt"]))

    match op:
        case '+':
            return num1 + num2

        case '-':
            return num1 - num2

        case '*':
            return num1 * num2

        case '/': return num1 / num2

def rerun(): # Asks if the user wants to do another operation, loops itselfsdsf
    while True:
        user_input = safeinput(prompt(lan["rerun"])).lower()
        if user_input == 'y':
            main()
        elif user_input == 'n':
            print(lan["goodbye"])
            break

# FUNCTIONS END #'


# MAIN #
welcome()
lan = data[lancheck(languagegrabber(), lanlister(data))]
main()
rerun()