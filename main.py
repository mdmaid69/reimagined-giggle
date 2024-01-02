def is_palindrome(s):
        return s == s[::-1]
def find_common_elements(list1, list2):
        return set(list1) & set(list2)