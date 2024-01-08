import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()