import platform
def get_os_info():
        return platform.uname()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)