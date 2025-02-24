
#| IMPORTS |#

## JSON import and setup

import json

with open('mortgagecalc.json', 'r') as file:
    MSG = json.load(file)

#| VARIABLES |#

LINE_STARTER = '==>'

#| FUNCTIONS |#

def starter(message):
    '''Formats all new lines to start with the line starter string
    '''
    return f"{LINE_STARTER} {message.format(starter = LINE_STARTER)}"

def input_clean(user_input):
    '''Cleans up input by removing allowed characters
    '''
    char_to_replace = ' %$,'
    for char in char_to_replace:
        user_input = user_input.replace(char, '')
    return user_input


def get_loan_amount():
    '''Manages the flow of other functions to get loan amount from user,
    checks that it is correct, and returns it as a float.
    '''
    print(starter(MSG["amount_wel"]))
    while True:
        loan_amount = input(starter(MSG['amount_inp']))
        loan_amount = input_clean(loan_amount)
        loan_amount_float = float_check(loan_amount, 'amount')

        if loan_amount_float == 0:
            print(starter(MSG['amount_zero']))
        elif loan_amount_float != 'x':
            break
    return loan_amount_float

def float_check(user_input, key):
    '''Checks input and performs float conversion if able to
    '''
    if '_' not in user_input:
        try:
            return float(user_input)
        except ValueError:
            error_msg = (
                MSG[f'{key}_blank'] if user_input == ''
                else MSG[f'{key}_float']
            )
            print(starter(error_msg))
            return 'x'
    else:
        print(starter(MSG['und']))
        return 'x'

def get_apr():
    '''Manages the flow of other functions to get APR from user,
    checks that it is correct, and converts it to a float.
    '''
    while True :
        apr_input = input(starter(MSG['apr_inp']))
        apr_input = input_clean(apr_input)
        apr = float_check(apr_input, 'apr')
        if apr != 'x':
            apr = convert_apr(apr)
            break
    return apr, apr_input

def convert_apr(apr_percentage):
    '''Converts yearly interest rate from a percent to a decimal
    '''
    return (apr_percentage / 100) / 12

def get_duration_and_check(key):
    '''Gets duration of loan from user, checks it, and returns it as an integer
    '''
    while True:
        raw_duration = input(starter(MSG[f'{key}_inp']))

        if raw_duration == '':
            return 0
        if '.' not in raw_duration:
            if raw_duration.isdigit():
                return int(raw_duration)
            print(starter(MSG[f'{key}_num']))
        else:
            print(starter(MSG[f'{key}_dec']))

## Gets loan duration and returns it correctly formatted

def get_loan_duration():
    '''Manages functions to get year duration and months duration.
    returns the total loan duration in months.
    '''
    print(starter(MSG['len_year']))
    while True:
        year_dur_int = get_duration_and_check('year')
        mon_dur_int = get_duration_and_check('mon')
        loan_duration_months = comb_months_years(year_dur_int, mon_dur_int)

        if loan_duration_months == 0:
            print(starter(MSG['len_zero']))
        else:
            break
    return loan_duration_months


def comb_months_years(years, months):
    '''Takes loan duration in years and months as arguments.


    Converts loan duration in years to months then returns
    total duration in months
    '''
    return (years * 12) + months

def calculate_equation(loan_amount, monthly_rate, months):
    '''Using the loan amount, monthly rate, and total
    length of the loan in months,

    this function calculates the monthly payment, total
    payments, and total interest. 

    Returns monthly payment, total payments, and total interest
    '''
    if monthly_rate == 0:
        monthly_payment = loan_amount / months
    else:
        monthly_payment = round(
            loan_amount * (
                monthly_rate / (
                    1 - (1 + monthly_rate) ** (-months)
                        )
                    ), 2
                )

    total_payments = round(monthly_payment * months, 2)
    total_interest = round(total_payments - loan_amount, 2)
    return monthly_payment, total_payments, total_interest

def print_results(results):
    '''Prints all results to the user using a list as an argument
    Make sure the list is organized correctly.
    '''
    print(
        starter(
            MSG['results'].format(
                monthly = results[0],
                total = results[1],
                interest = results[2],
                amount = results[3],
                length = results[4],
                apr = results[5],
                starter = LINE_STARTER
            )
        )
    )

def run_program():
    '''Manages all functions and provides flow control for the program
    '''
    print(starter(MSG['welcome']))
    amount = get_loan_amount()
    rate, raw_apr = get_apr()
    length = get_loan_duration()
    args = (*calculate_equation(amount, rate, length), amount, length, raw_apr)
    print_results(args)

run_program()