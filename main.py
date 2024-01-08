import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def is_palindrome(s):
        return s == s[::-1]