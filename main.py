import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def is_palindrome(s):
        return s == s[::-1]