import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))