import random
def roll_die():
        return random.randint(1, 6)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])