import array
def get_array_as_bytearray(array):
        return bytearray(array)
def is_palindrome(s):
        return s == s[::-1]