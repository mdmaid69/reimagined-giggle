import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
i = 0
while i < 5:
        print(i)
        i += 1