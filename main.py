import os
def get_current_working_directory():
        return os.getcwd()
def is_palindrome(s):
        return s == s[::-1]