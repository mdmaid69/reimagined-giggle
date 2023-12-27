import platform
def get_python_version():
        return platform.python_version()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])