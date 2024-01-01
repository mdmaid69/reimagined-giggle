import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def is_palindrome(s):
        return s == s[::-1]