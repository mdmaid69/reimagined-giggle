import platform
def get_os_info():
        return platform.uname()
def greet(name):
        print(f"Hello, {name}!")