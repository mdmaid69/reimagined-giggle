import array
def get_array_as_memoryview(array):
        return memoryview(array)
def is_palindrome(s):
        return s == s[::-1]