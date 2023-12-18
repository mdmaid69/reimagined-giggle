import collections
def create_stack():
        return collections.deque()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()