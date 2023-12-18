import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def is_palindrome(s):
        return s == s[::-1]