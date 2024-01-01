import platform
def get_python_version():
        return platform.python_version()
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)