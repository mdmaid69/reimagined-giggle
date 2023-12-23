import random
def generate_random_number(start, end):
        return random.randint(start, end)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))