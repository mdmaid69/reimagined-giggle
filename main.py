def is_palindrome(s):
        return s == s[::-1]
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)