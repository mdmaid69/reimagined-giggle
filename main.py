def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import sys
def add_to_python_path(path):
        sys.path.append(path)