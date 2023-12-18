import random
def generate_random_choice(choices):
        return random.choice(choices)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b