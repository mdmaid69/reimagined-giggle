n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import platform
def get_python_version():
        return platform.python_version()