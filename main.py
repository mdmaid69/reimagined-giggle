def is_palindrome(s):
        return s == s[::-1]
import os
def get_file_size(filename):
        return os.path.getsize(filename)