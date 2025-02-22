
#| IMPORTS |#

## JSON import and setup

import json

with open('mortgagecalc.json', 'r') as file:
    MSG = json.load(file)

#| FUNCTIONS |#

def emphasize(message):
    return (f">> {message}")

## Gets loan amount and returns it correctly formatted as an integer

def get_loan_amount():
    print(emphasize(MSG["amount_wel"]))
    while True:
        loan_amount = input(emphasize(MSG['amount_inp']))

        loan_amount = loan_amount.replace(',', '') # removing ',' ex: 10,000
        loan_amount = loan_amount.replace(' ', '') # removing ' ' ex: "10,000 "

        if loan_amount.isdigit():
            loan_amount_int = int(loan_amount)
            if loan_amount_int != 0:
                break
            else:
                print(emphasize(MSG['amount_zero']))
        else: 
            print(MSG['amount_num'])
    return int(loan_amount_int)

## Gets APR from user and returns it as an integer

def get_apr():

    while True:
        apr_input = input(emphasize(MSG['apr_input']))

        apr_input = apr_input.replace('%', '') # removing % ex: 15% -> 15
        apr_input = apr_input.replace(' ', '') # removing ' ' ex: "15 " -> "15"
        if apr_input.isdigit():

            apr = convert_apr(int(apr_input))
            break

        if '_' not in apr_input: # I eccidentally entered 5_3 once and it coerced it into 53 as float
            try:
                apr = convert_apr(float(apr_input))
                break
            except ValueError:
                print(emphasize(MSG['apr_float']))
    return apr

## converts yearly APR from percentage to monthly decimal

def convert_apr(apr_percentage):
    return (apr_percentage / 100) / 12

def get_loan_duration():
    while True:
        print(emphasize(MSG['len_year']))
        while True:
            year_duration_input =input(emphasize(MSG['year_inp']))
            if '.' not in year_duration_input:
                if year_duration_input.isdigit():
                    year_duration_int = int(year_duration_input)
                    break
                else:
                    print(emphasize(MSG['len_num']))
            else: 
                print('Please enter only whole numbers without decimal points.\n'
                    'For example if your loan amount is 7.5 years,'
                    'please just enter 7 now and dont worry,\n'
                    'you will be asked later to enter the remaining months.')
        while True:
            month_duration_input = input('please give the remaing time left in months,\n'
                                        'if no remaining enter 0 or click enter')
            if month_duration_input == '':
                month_duration_int = 0
                break
            if '.' not in month_duration_input:
                if month_duration_input.isdigit() or month_duration_input == '0':
                    month_duration_int = int(month_duration_input)
                    break
                else:
                    print('Please enter only numbers - placeholder')
            else:
                print('Please enter only whole numbers without decimal points.\n'
                    'for example, if the remaining months for your loan is 3.7 months,'
                    'please enter 4. Rounding up or down is up to your discretion.\n'
                    'We will not be calculating for remaining weeks or days.')
        loan_duration_months = combine_months_and_years(year_duration_int, month_duration_int)
        if loan_duration_months == 0:
            print('years and months cannot be 0')
        else:
            break
    return loan_duration_months

def combine_months_and_years(years, months):
    return (years * 12) + months

def calculate_equation(loan_amount, months, monthly_rate):
    monthy_payment = round(loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** (-months))), 2)
    total_payments = round(monthy_payment * months, 2)
    total_interest = round(total_payments - loan_amount, 2)
    return monthy_payment, total_payments, total_interest

def run_program():
    print(emphasize(MSG['welcome']))
    loan_amount = get_loan_amount()
    interest_rate = get_apr()
    loan_length = get_loan_duration()


# monthly_payment, total_payments, total_interest = calculate_equation(get_loan_amount(), get_loan_duration(), get_apr())
# print(monthly_payment)
# print(total_payments)
# print(total_interest)
run_program()