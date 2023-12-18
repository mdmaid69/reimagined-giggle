import collections
def create_ordered_dict():
        return collections.OrderedDict()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()