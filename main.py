import random
print(random.randint(0, 100))
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))