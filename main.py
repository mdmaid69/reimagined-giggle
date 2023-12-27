def is_palindrome(s):
        return s == s[::-1]
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)