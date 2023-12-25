import random
def generate_random_number(start, end):
        return random.randint(start, end)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])