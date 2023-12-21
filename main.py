import array
def get_array_as_repr(array):
        return repr(array)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()