import random
def roll_die():
        return random.randint(1, 6)
def find_union(list1, list2):
        return set(list1) | set(list2)