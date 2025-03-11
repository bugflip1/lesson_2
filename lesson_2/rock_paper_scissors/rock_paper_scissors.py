
#| Imports |#

import random
import os
import json

## JSON Setup
with open('rps.json', 'r') as file:
    MSG = json.load(file)

#| Variables |#

STARTING_SCORE = 0
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
BEATS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'spock': ['scissors', 'rock'],
    'lizard': ['paper', 'spock']
    }

#| Functions |#

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt(message):
    print(f"==> {message}")

def get_round_winner(player, computer):
    if computer in BEATS[player]:
        return 'user'
    if player in BEATS[computer]:
        return 'computer'
    return None

def format_result_message(winner, user_choice, computer_choice):
    if winner == 'user':
        message = MSG["usr_won"].format(
            usr_choice = user_choice,
            win_msg = MSG["win_messages"][user_choice][computer_choice],
            comp_choice = computer_choice
            )

        announce_win = MSG["announce_win"]

        return announce_win, message

    if winner == 'computer':
        message = MSG["comp_won"].format(
            usr_choice = user_choice,
            win_msg = MSG["win_messages"][computer_choice][user_choice],
            comp_choice = computer_choice
            )

        announce_loss = MSG["announce_loss"]

        return announce_loss, message

    tie_message = MSG["tie"].format(
        usr_choice = user_choice,
        comp_choice = computer_choice
        )

    announce_tie = MSG["announce_tie"]

    return announce_tie, tie_message

def get_user_choice():
    return input().lower()

def display_pre_messages(user_score, computer_score):
    prompt(MSG["choice_prompt"].format(choices = ", ".join(VALID_CHOICES)))
    prompt(MSG["choice_instruct"])
    prompt(MSG["usr_score"].format(score = user_score))
    prompt(MSG["comp_score"].format(score = computer_score))

def validate_user_choice(user_input):
    if user_input in VALID_CHOICES:
        return user_input
    if user_input == 'sc':
        return VALID_CHOICES[2]
    for choice in VALID_CHOICES:
        if choice == VALID_CHOICES[2]:
            continue
        if user_input == choice[0]:
            return choice
    return False

def generate_computer_choice():
    return random.choice(VALID_CHOICES)

def run_one_round(player_score, com_score):
    while True:
        clear_terminal()
        display_pre_messages(player_score, com_score)
        user_choice = get_user_choice()
        validated_choice = validate_user_choice(user_choice)
        if validated_choice:
            break

    computer_choice = generate_computer_choice()
    winner = get_round_winner(validated_choice, computer_choice)
    announce_result, result_message = format_result_message(
        winner, validated_choice, computer_choice
        )
    prompt(announce_result)
    prompt(result_message)
    return winner

def display_welcome():
    clear_terminal()
    prompt(MSG["welcome_instruct"])
    prompt(MSG["cont_welcome"])
    input()

def user_init_next_round():
    prompt(MSG["next_round"])
    input()

def ask_to_rerun():
    while True:
        prompt(MSG["rerun_prompt"])
        rerun_input = input()
        if rerun_input != '':
            if rerun_input[0] == 'y':
                return True
            if rerun_input[0] == 'n':
                return False
        prompt(MSG["invalid_rerun"])

def increment_winner(winner, usr_scr, comp_scr):
    if winner == 'user':
        return usr_scr + 1, comp_scr
    if winner == 'computer':
        return usr_scr, comp_scr + 1
    return usr_scr, comp_scr

def get_game_winner(user_score, computer_score):
    if user_score > computer_score:
        return 'user'
    return 'computer'

def display_game_winner(user_score, computer_score, total_game_winner):
    if total_game_winner == 'user':
        prompt(MSG["total_win"])
    else:
        prompt(MSG["total_loss"])
    prompt(MSG["total_score"].format(
        usr_wins = user_score,
        comp_wins = computer_score
        )
    )

def user_init_game_end_msg():
    prompt(MSG["cont_game"])
    input()

def run_one_game(usr_scr, comp_scr):
    while True:
        round_winner = run_one_round(usr_scr, comp_scr)
        usr_scr, comp_scr = increment_winner(
            round_winner, usr_scr, comp_scr
            )
        if comp_scr == 3 or usr_scr == 3:
            user_init_game_end_msg()
            clear_terminal()
            return usr_scr, comp_scr
        user_init_next_round()

def run_program():
    display_welcome()
    while True:
        usr_score, comp_score = run_one_game(STARTING_SCORE, STARTING_SCORE)
        game_winner = get_game_winner(usr_score, comp_score)
        display_game_winner(usr_score, comp_score, game_winner)
        if not ask_to_rerun():
            break

#| Main |#

run_program()
