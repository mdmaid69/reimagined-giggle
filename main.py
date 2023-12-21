text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import platform
def get_os_info():
        return platform.uname()