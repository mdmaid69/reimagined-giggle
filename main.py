import platform
def get_os_info():
        return platform.uname()
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))