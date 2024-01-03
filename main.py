import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)