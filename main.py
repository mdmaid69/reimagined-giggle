import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()