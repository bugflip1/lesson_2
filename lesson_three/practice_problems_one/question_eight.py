flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
new_names = ['Dino', 'Hoppy']

def add_multiple_elements_to_list(original_list, new_elements):
    original_list.extend(new_elements)
    return original_list

print(add_multiple_elements_to_list(flintstones, new_names))