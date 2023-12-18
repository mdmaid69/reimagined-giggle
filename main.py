import os
def remove_directory(path):
        os.rmdir(path)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)