import sys
def print_python_version():
        print(sys.version)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))