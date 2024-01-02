import random
def generate_random_choice(choices):
        return random.choice(choices)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])