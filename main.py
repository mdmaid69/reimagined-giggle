import random
def generate_random_number(start, end):
        return random.randint(start, end)
n = 10
print("Square numbers:", [x**2 for x in range(n)])