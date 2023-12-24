import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()