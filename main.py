import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()