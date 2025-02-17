# IMPORTS #

# JSON import and setup
import json

# Open the JSON file for reading
with open('calculator/calculator.json', 'r') as file:
    data = json.load(file)

# FUNCTIONS #

def welcome(): # Welcome message
    print(prompt(data["english"]["welcome_messages"]))

def prompt(message): # Adds a arrow to the start of messages
    return f"==> {message}"      

def lanassign(): # Assigns language grabber value to a variable and maps it data
    return data[languagegrabber()]

def languagegrabber(): # Language grabber
    lan = input(prompt(data["english"]["langrabber"])).lower()
    return lan

def main(): # Main function

    # Ask the user for the first number
    number1 = input(prompt(lan["numoneprompt"]))
    while not is_numeric(number1):
        number1 = input(prompt(lan["invalidnum"]))

    # Ask the user for the second number
    number2 = input(prompt(lan["numtwoprompt"]))
    while not is_numeric(number2):
        number2 = input(prompt(lan["invalidnum"]))


    # Ask the user for the operation to perform
    operation = input(prompt(lan["opprompt"]))

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
    match op:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2

        case '*':
            return num1 * num2

        case '/':
            return num1 / num2

        case _:
            user_operation = input(prompt(
                lan["invalidop"]
                ))
            return operation_complete(num1, num2, user_operation)
        
def rerun(): # Asks if the user wants to do another operation, loops itself
    user_input = input(prompt(lan["rerun"]))
    if user_input.lower() == 'y':
        main()
        rerun()
    elif user_input.lower() == 'n':
        print(data["goodbye"])

# FUNCTIONS END #'


# MAIN #
welcome()
lan = lanassign()
main()
rerun()