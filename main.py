import platform
def get_python_version():
        return platform.python_version()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])