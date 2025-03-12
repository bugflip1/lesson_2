str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def exclamation_mark_at_end(string):
    return string.endswith('!')

print(exclamation_mark_at_end(str1))
print(exclamation_mark_at_end(str2))