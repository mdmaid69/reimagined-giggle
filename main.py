import platform
def get_python_version():
        return platform.python_version()
def is_palindrome(s):
        return s == s[::-1]