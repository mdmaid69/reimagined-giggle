import random
def generate_random_choice(choices):
        return random.choice(choices)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))