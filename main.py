import os
def list_files_in_directory(path):
        return os.listdir(path)
def is_palindrome(s):
        return s == s[::-1]