import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)