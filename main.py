import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def find_common_elements(list1, list2):
        return set(list1) & set(list2)