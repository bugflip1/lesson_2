
#| IMPORTS |#

import json

with open('mortgage_calc_messages.json', 'r') as file:
    MSG = json.load(file)

import os

#| VARIABLES |#

LINE_STARTER = '==>'
DECIMAL_POINTS = 2
MONTHS_IN_YEAR = 12

#| FUNCTIONS |#

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_string_for_two_decimal_places(input_string):
    if '.' in input_string:
        decimals = input_string.split('.')[1]
        return len(decimals) > 2
    return False

def format_messages_with_prefix(message):
    return f"{LINE_STARTER} {message.format(starter = LINE_STARTER)}"

def remove_special_characters(user_input):
    char_to_replace = ' %$,'
    for char in char_to_replace:
        user_input = user_input.replace(char, '')
    return user_input


def get_loan_amount():
    print(format_messages_with_prefix(MSG["amount_wel"]))
    while True:
        user_amount = input(format_messages_with_prefix(MSG['amount_inp']))
        user_amount = remove_special_characters(user_amount)
        amount_float = validate_input_and_display_errors(user_amount, 'amount')

        if amount_float is None:
            continue
        if amount_float == 0:
            print(format_messages_with_prefix(MSG['amount_zero']))
            continue
        if amount_float < 0:
            print(format_messages_with_prefix(MSG['amount_neg']))
            continue
        break
    return amount_float

def validate_input_and_display_errors(user_input, key):
    if '_' in user_input:
        print(format_messages_with_prefix(MSG['und']))
        return None
    if check_string_for_two_decimal_places(user_input):
        print(format_messages_with_prefix(MSG[f'{key}_two_dec']))
        return None
    try:
        return float(user_input)
    except ValueError:
        error_msg = (
            MSG[f'{key}_blank'] if user_input == ''
            else MSG[f'{key}_float']
        )
        print(format_messages_with_prefix(error_msg))
        return None

def get_apr():
    while True:
        apr_input = input(format_messages_with_prefix(MSG['apr_inp']))
        apr_input = remove_special_characters(apr_input)
        apr = validate_input_and_display_errors(apr_input, 'apr')
        if apr is None:
            continue
        if apr < 0:
            print(format_messages_with_prefix(MSG['apr_neg']))
            continue
        apr = convert_apr(apr)
        break
    return apr, apr_input

def convert_apr(apr_percentage):
    return (apr_percentage / 100) / MONTHS_IN_YEAR

def get_duration_and_check(key):
    while True:
        raw_duration = input(format_messages_with_prefix(MSG[f'{key}_inp']))

        duration_converted, looper = check_duration_and_display_error(
            raw_duration, key
            )
        if not looper:
            return duration_converted

def check_duration_and_display_error(duration_input, key):
    if duration_input == '':
        return 0, False
    if duration_input.isdigit():
        return int(duration_input), False
    if '.' in duration_input:
        print(format_messages_with_prefix(MSG[f'{key}_dec']))
        return '', True
    print(format_messages_with_prefix(MSG[f'{key}_num']))
    return '', True

def get_loan_duration():
    print(format_messages_with_prefix(MSG['len_year']))
    while True:
        year_dur_int = get_duration_and_check('year')
        mon_dur_int = get_duration_and_check('mon')
        loan_duration_months = comb_months_years(year_dur_int, mon_dur_int)

        if loan_duration_months == 0:
            print(format_messages_with_prefix(MSG['len_zero']))
        else:
            return loan_duration_months


def comb_months_years(years, months):
    return (years * MONTHS_IN_YEAR) + months

def calculate_equation(loan_amount, monthly_rate, months):
    if monthly_rate == 0:
        monthly_payment = loan_amount / months
    else:
        monthly_payment = round(
            loan_amount * (
                monthly_rate / (
                    1 - (1 + monthly_rate) ** (-months)
                        )
                    ), DECIMAL_POINTS
                )

    total_payments = round(monthly_payment * months, DECIMAL_POINTS)
    total_interest = round(total_payments - loan_amount, DECIMAL_POINTS)
    return monthly_payment, total_payments, total_interest

def print_results(results):
    print(
        format_messages_with_prefix(
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

def run_calculator():
    amount = get_loan_amount()
    rate, raw_apr = get_apr()
    length = get_loan_duration()
    args = (*calculate_equation(amount, rate, length), amount, length, raw_apr)
    print_results(args)

def ask_to_rerun():
    while True:
        rerun_input = input(format_messages_with_prefix(
            MSG['rerun_prompt']
            )).lower()
        if rerun_input != '':
            if rerun_input[0] == 'y':
                return True
            if rerun_input[0] == 'n':
                return False
        print(format_messages_with_prefix((MSG['rerun_invalid'])))

def run_program():
    print(format_messages_with_prefix(MSG['welcome']))
    while True:
        clear_terminal()
        run_calculator()
        if not ask_to_rerun():
            break

#| Main Program |#
run_program()
