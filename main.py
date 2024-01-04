import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import platform
def get_python_version():
        return platform.python_version()