import random
def roll_die():
        return random.randint(1, 6)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))