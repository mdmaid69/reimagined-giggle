def is_palindrome(s):
        return s == s[::-1]
import platform
def get_os_info():
        return platform.uname()