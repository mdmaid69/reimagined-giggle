import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()