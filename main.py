import array
def get_array_buffer_info(array):
        return array.buffer_info()
def is_palindrome(s):
        return s == s[::-1]