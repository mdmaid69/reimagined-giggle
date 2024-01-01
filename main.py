import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()