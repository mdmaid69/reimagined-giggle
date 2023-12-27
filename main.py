import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def is_palindrome(s):
        return s == s[::-1]