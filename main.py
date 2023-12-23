def is_palindrome(s):
        return s == s[::-1]
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()