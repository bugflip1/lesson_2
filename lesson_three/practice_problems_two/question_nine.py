ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

additional_ages = {'Marilyn': 22, 'Spot': 237}

def add_new_people_to_age_dict(initial_dict, dict_to_add):
    initial_dict.update(dict_to_add)
    return initial_dict

print(add_new_people_to_age_dict(ages, additional_ages))