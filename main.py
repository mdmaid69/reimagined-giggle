import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def extend_array(array, iterable):
        array.extend(iterable)