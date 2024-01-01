import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()