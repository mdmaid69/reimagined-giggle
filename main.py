import os
def get_environment_variable(var):
        return os.getenv(var)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)