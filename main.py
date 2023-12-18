import sys
def add_to_python_path(path):
        sys.path.append(path)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])