import os
def remove_directory(path):
        os.rmdir(path)
def is_palindrome(s):
        return s == s[::-1]