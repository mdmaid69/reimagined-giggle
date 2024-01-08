import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def is_palindrome(s):
        return s == s[::-1]