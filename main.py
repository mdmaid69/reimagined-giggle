import platform
def get_python_version():
        return platform.python_version()
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))