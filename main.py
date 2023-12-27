n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import random
def roll_die():
        return random.randint(1, 6)