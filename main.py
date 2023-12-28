import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def is_palindrome(s):
        return s == s[::-1]