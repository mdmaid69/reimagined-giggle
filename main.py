list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"