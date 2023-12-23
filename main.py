import sys
def print_python_version():
        return sys.version
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b