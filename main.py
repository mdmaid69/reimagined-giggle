import sys
def add_to_python_path(path):
        sys.path.append(path)
def is_palindrome(s):
        return s == s[::-1]