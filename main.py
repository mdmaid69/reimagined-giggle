def is_palindrome(s):
        return s == s[::-1]
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable