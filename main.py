n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)