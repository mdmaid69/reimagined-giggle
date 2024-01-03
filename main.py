import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))