import os
def get_environment_variable(var):
        return os.getenv(var)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b