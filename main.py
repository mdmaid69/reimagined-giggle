n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import sys
def add_to_python_path(path):
        sys.path.append(path)