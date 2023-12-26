import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import collections
def create_queue():
        return collections.deque()