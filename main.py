import platform
def get_os_info():
        return platform.uname()
n = 10
print("Square numbers:", [x**2 for x in range(n)])