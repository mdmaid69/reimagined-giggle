text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import platform
def get_python_version():
        return platform.python_version()