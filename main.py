import sys
def add_to_python_path(path):
        sys.path.append(path)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)