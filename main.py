import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)