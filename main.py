import sys
def add_to_python_path(path):
        sys.path.append(path)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])