def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import platform
def get_python_version():
        return platform.python_version()