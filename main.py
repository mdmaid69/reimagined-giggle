import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def is_palindrome(s):
        return s == s[::-1]