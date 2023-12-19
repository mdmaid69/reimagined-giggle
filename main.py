import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)