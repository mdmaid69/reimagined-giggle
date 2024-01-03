import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def is_palindrome(s):
        return s == s[::-1]