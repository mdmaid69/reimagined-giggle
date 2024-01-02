import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)