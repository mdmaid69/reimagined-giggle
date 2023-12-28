import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()