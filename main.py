import random
def generate_random_choice(choices):
        return random.choice(choices)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])