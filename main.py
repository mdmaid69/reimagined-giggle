import os
def get_file_size(filename):
        return os.path.getsize(filename)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)