import random
def generate_random_choice(choices):
        return random.choice(choices)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)