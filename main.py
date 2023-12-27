import sys
def add_to_python_path(path):
        sys.path.append(path)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))