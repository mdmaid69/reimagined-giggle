import array
def get_bytes_from_array(array):
        return array.tobytes()
def is_palindrome(s):
        return s == s[::-1]