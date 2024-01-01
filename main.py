def is_palindrome(s):
        return s == s[::-1]
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)