import random
def generate_random_number(start, end):
        return random.randint(start, end)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])