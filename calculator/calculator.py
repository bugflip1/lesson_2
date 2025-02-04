# Is numeric function, really checks for float.
def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

    try:
        int(s)
        return True
    except ValueError:
        return False

def conv_int(num1, num2):
    return float(num1), float(num2)

def prompt(message):
    return f"==> {message}"

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
                'Please enter an appropriate operation!\n'
                '(+, -, *, or /)'
                ))
            return operation_complete(num1, num2, user_operation)

# Welcome
print('Welcome to Calculator!')

# Ask the user for the first number
number1 = input(prompt("What's the first number?\n"))
while not is_numeric(number1):
    number1 = input(prompt("Please enter a valid number!\n"))

# Ask the user for the second number
number2 = input(prompt("What's the second number?\n"))
while not is_numeric(number2):
    number1 = input(prompt("Please enter a valid number!\n"))


# Ask the user for the operation to perform
operation = input(prompt(
    "What operation would you like to perform?\n"
    '"+" for addition\n"-" for subtraction\n"*" for multiplication\n'
    ""/" for division\nEnter here: "
    ))

# Perform the operation on the two numbers
number1, number2 = conv_int(number1, number2)

# Print the result to the terminal
print(f"The result is: {operation_complete(number1, number2, operation)}")
