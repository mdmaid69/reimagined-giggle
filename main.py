def is_palindrome(s):
        return s == s[::-1]
import os
def get_environment_variable(var):
        return os.getenv(var)