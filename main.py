import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])