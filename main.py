def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import sys
def print_python_version():
        print(sys.version)