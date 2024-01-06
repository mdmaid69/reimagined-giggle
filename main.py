import platform
def get_python_version():
        return platform.python_version()
n = 10
print("Square numbers:", [x**2 for x in range(n)])