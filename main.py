import platform
def get_python_version():
        return platform.python_version()
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])