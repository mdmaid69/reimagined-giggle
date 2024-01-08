import platform
def get_os_info():
        return platform.uname()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])