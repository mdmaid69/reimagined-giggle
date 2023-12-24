import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()