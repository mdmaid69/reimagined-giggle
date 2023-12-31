def is_palindrome(s):
        return s == s[::-1]
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)