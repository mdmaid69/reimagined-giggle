import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def get_array_itemsize(array):
        return array.itemsize