import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def is_palindrome(s):
        return s == s[::-1]