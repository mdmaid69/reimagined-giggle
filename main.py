import array
def get_array_slice(array, i, j):
        return array[i:j]
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()