import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def is_palindrome(s):
        return s == s[::-1]