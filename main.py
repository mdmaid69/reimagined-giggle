import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))