def is_palindrome(s):
        return s == s[::-1]
import os
def change_working_directory(path):
        os.chdir(path)