import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])