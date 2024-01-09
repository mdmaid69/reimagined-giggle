import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)