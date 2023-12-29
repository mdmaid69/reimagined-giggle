import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)