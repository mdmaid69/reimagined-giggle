import platform
def get_os_info():
        return platform.uname()
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])