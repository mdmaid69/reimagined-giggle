import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def is_palindrome(s):
        return s == s[::-1]