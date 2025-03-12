def is_an_ip_number(this_is_a_filler_so_the_file_isnt_red_in_vscode):
    return this_is_a_filler_so_the_file_isnt_red_in_vscode

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) == 4:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return True

    return False