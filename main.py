def is_palindrome(s):
        return s == s[::-1]
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)