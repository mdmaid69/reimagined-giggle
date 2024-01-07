import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()