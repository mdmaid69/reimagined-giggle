import sys
def print_python_version():
        print(sys.version)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)