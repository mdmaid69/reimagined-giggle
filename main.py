import sys
def add_to_python_path(path):
        sys.path.append(path)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])