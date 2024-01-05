import random
def roll_die():
        return random.randint(1, 6)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)