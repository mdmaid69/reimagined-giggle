import platform
def get_os_info():
        return platform.uname()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])