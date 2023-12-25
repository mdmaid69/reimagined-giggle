import sys
def add_to_python_path(path):
        sys.path.append(path)
n = 10
print("Powers of 2:", [2**x for x in range(n)])