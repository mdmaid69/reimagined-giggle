n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import os
def list_files_in_directory(path):
        return os.listdir(path)