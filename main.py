import random
def roll_die():
        return random.randint(1, 6)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])